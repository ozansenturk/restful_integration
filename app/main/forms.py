from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired


class ReportForm(FlaskForm):

    fromDate = DateField('From Date', format='%Y-%m-%d')
    toDate = DateField('To Date', format='%Y-%m-%d')

    merchant = StringField('Merchant')
    acquirer = StringField('Acquirer')
    submit = SubmitField('Process')