from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class TextForm(FlaskForm):
    text_input = TextAreaField('TextInput', validators=[DataRequired()])
    text_option = RadioField('Text Analytics', choices=[('lemmitize', 'lemmitize'),
                                                        ('pos_tag', 'pos_tag'), ('entities', 'entities')])
    submit = SubmitField('Process')