from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Vokabelblock, Vokabel

routes_bp = Blueprint('routes_bp', __name__)

@routes_bp.route('/')
def index():
    return render_template('index.html')

@routes_bp.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        name = request.form['name']
        sprache1 = request.form['language1']
        sprache2 = request.form['language2']

        if Vokabelblock.validate_fields(name, sprache1, sprache2):
            new_block = Vokabelblock(name=name, sprache1=sprache1, sprache2=sprache2)
            db.session.add(new_block)
            db.session.commit()
            flash('Vokabelliste erfolgreich erstellt!', 'success')
            return redirect(url_for('routes_bp.settings'))

    vocab_blocks = Vokabelblock.query.all()
    return render_template('settings.html', vocab_blocks=vocab_blocks)

@routes_bp.route('/edit_block/<int:block_id>', methods=['GET', 'POST'])
def edit_block(block_id):
    block = Vokabelblock.query.get_or_404(block_id)
    if request.method == 'POST':
        block.name = request.form['name']
        block.sprache1 = request.form['language1']
        block.sprache2 = request.form['language2']
        db.session.commit()
        flash('Vokabelliste erfolgreich bearbeitet!', 'success')
        return redirect(url_for('routes_bp.settings'))
    return render_template('edit_block.html', block=block)

@routes_bp.route('/delete_block/<int:block_id>', methods=['POST'])
def delete_block(block_id):
    block = Vokabelblock.query.get_or_404(block_id)
    db.session.delete(block)
    db.session.commit()
    flash('Vokabelliste erfolgreich gelöscht!', 'success')
    return redirect(url_for('routes_bp.settings'))

@routes_bp.route('/manage_vocab/<int:block_id>', methods=['GET', 'POST'])
def manage_vocab(block_id):
    block = Vokabelblock.query.get_or_404(block_id)
    if request.method == 'POST':
        sprache1 = request.form['sprache1']
        sprache2 = request.form['sprache2']
        new_vocab = Vokabel(block_id=block.id, sprache1=sprache1, sprache2=sprache2)
        db.session.add(new_vocab)
        db.session.commit()
        flash('Vokabel erfolgreich hinzugefügt!', 'success')
        return redirect(url_for('routes_bp.manage_vocab', block_id=block.id))

    vocab_list = Vokabel.query.filter_by(block_id=block.id).all()
    return render_template('manage_vocab.html', block=block, vocab_list=vocab_list)

@routes_bp.route('/edit_vocab/<int:vocab_id>', methods=['GET', 'POST'])
def edit_vocab(vocab_id):
    vocab = Vokabel.query.get_or_404(vocab_id)
    if request.method == 'POST':
        vocab.sprache1 = request.form['sprache1']
        vocab.sprache2 = request.form['sprache2']
        db.session.commit()
        flash('Vokabel erfolgreich bearbeitet!', 'success')
        return redirect(url_for('routes_bp.manage_vocab', block_id=vocab.block_id))
    return render_template('edit_vocab.html', vocab=vocab)

@routes_bp.route('/delete_vocab/<int:vocab_id>', methods=['POST'])
def delete_vocab(vocab_id):
    vocab = Vokabel.query.get_or_404(vocab_id)
    block_id = vocab.block_id
    db.session.delete(vocab)
    db.session.commit()
    flash('Vokabel erfolgreich gelöscht!', 'success')
    return redirect(url_for('routes_bp.manage_vocab', block_id=block_id))

@routes_bp.route('/practice', methods=['GET', 'POST'])
@routes_bp.route('/practice/<int:block_id>', methods=['GET', 'POST'])
def practice(block_id=None):
    vocab_blocks = Vokabelblock.query.all()

    if not vocab_blocks:
        return redirect(url_for('routes_bp.settings'))

    selected_block = None
    current_vocab = None
    evaluation = None
    vocab_index = 0
    all_vocab_queried = False
    total_vocab = 0
    direction = 'normal'  # Standardwert setzen

    if block_id or (len(vocab_blocks) == 1):
        if not block_id:
            block_id = vocab_blocks[0].id
        selected_block = Vokabelblock.query.get_or_404(block_id)
        vocab_list = Vokabel.query.filter_by(block_id=block_id).all()
        total_vocab = len(vocab_list)

        if request.method == 'POST':
            action = request.form['action']
            vocab_index = int(request.form.get('vocab_index', 0))
            direction = request.form.get('direction', 'normal')
            current_vocab = vocab_list[vocab_index] if vocab_list else None

            if action == 'evaluate':
                sprache2_input = request.form['sprache2'].strip().lower()
                if direction == 'normal':
                    evaluation = {
                        'correct': sprache2_input == current_vocab.sprache2.strip().lower()
                    }
                else:
                    evaluation = {
                        'correct': sprache2_input == current_vocab.sprache1.strip().lower()
                    }
            elif action == 'next':
                vocab_index += 1
                if vocab_index >= len(vocab_list):
                    all_vocab_queried = True
                    vocab_index = 0
                    current_vocab = None
                else:
                    current_vocab = vocab_list[vocab_index]
            elif action == 'retry':
                vocab_index = 0
                current_vocab = vocab_list[vocab_index] if vocab_list else None
                all_vocab_queried = False

        else:
            # GET-Anfrage
            direction = request.args.get('direction', 'normal')
            current_vocab = vocab_list[vocab_index] if vocab_list else None

    return render_template(
        'practice.html',
        vocab_blocks=vocab_blocks,
        selected_block=selected_block,
        current_vocab=current_vocab,
        evaluation=evaluation,
        vocab_index=vocab_index,
        all_vocab_queried=all_vocab_queried,
        total_vocab=total_vocab,
        direction=direction  # Variable übergeben
    )

@routes_bp.route('/quick_learn', methods=['GET', 'POST'])
@routes_bp.route('/quick_learn/<int:block_id>', methods=['GET', 'POST'])
def quick_learn(block_id=None):
    vocab_blocks = Vokabelblock.query.all()
    
    if not vocab_blocks:
        return redirect(url_for('routes_bp.settings'))
    
    selected_block = None
    current_vocab = None
    evaluation = None
    vocab_index = 0
    all_vocab_queried = False
    total_vocab = 0
    direction = 'normal'  # Standardrichtung
    
    if block_id or (len(vocab_blocks) == 1):
        if not block_id:
            block_id = vocab_blocks[0].id
        selected_block = Vokabelblock.query.get_or_404(block_id)
        vocab_list = Vokabel.query.filter_by(block_id=block_id).all()
        total_vocab = len(vocab_list)
        
        if request.method == 'POST':
            action = request.form['action']
            vocab_index = int(request.form.get('vocab_index', 0))
            direction = request.form.get('direction', 'normal')
            current_vocab = vocab_list[vocab_index]
            if action == 'know':
                evaluation = {'correct': True}
            elif action == 'dont_know':
                evaluation = {'correct': False}
            elif action == 'next':
                vocab_index += 1
                if vocab_index >= len(vocab_list):
                    all_vocab_queried = True
                    vocab_index = 0
                    current_vocab = None
                else:
                    current_vocab = vocab_list[vocab_index]
            elif action == 'retry':
                vocab_index = 0
                current_vocab = vocab_list[vocab_index]
                all_vocab_queried = False
        
        if not current_vocab and vocab_list:
            current_vocab = vocab_list[vocab_index]
    else:
        direction = request.args.get('direction', 'normal')
    
    return render_template(
        'quick_learn.html',
        vocab_blocks=vocab_blocks,
        selected_block=selected_block,
        current_vocab=current_vocab,
        evaluation=evaluation,
        vocab_index=vocab_index,
        all_vocab_queried=all_vocab_queried,
        total_vocab=total_vocab,
        direction=direction  # Richtung übergeben
    )