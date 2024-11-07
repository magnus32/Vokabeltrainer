from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class VokabelblockForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=15)])
    sprache1 = StringField('Sprache 1', validators=[DataRequired(), Length(min=2, max=15)])
    sprache2 = StringField('Sprache 2', validators=[DataRequired(), Length(min=2, max=15)])
    submit = SubmitField('Neuen Vokabelblock erstellen')