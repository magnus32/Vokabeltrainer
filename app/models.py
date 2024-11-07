from datetime import datetime, timezone
from flask import flash
from . import db

class Vokabelblock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15), nullable=False)
    sprache1 = db.Column(db.String(15), nullable=False)
    sprache2 = db.Column(db.String(15), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __init__(self, name, sprache1, sprache2):
        self.name = name
        self.sprache1 = sprache1
        self.sprache2 = sprache2

    @staticmethod
    def validate_fields(name, sprache1, sprache2):
        if not (2 <= len(name) <= 15):
            flash("Der Name muss zwischen 2 und 15 Zeichen lang sein.", "error")
            return False
        if not (2 <= len(sprache1) <= 15):
            flash("Sprache 1 muss zwischen 2 und 15 Zeichen lang sein.", "error")
            return False
        if not (2 <= len(sprache2) <= 15):
            flash("Sprache 2 muss zwischen 2 und 15 Zeichen lang sein.", "error")
            return False
        return True

class Vokabel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    block_id = db.Column(db.Integer, db.ForeignKey('vokabelblock.id'), nullable=False)
    sprache1 = db.Column(db.String(50), nullable=False)
    sprache2 = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    def __init__(self, block_id, sprache1, sprache2):
        self.block_id = block_id
        self.sprache1 = sprache1
        self.sprache2 = sprache2