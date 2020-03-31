from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SubmitField, IntegerField, validators
from wtforms.validators import DataRequired


class ReportForm(FlaskForm):

    fromDate = DateField('From Date', format='%Y-%m-%d')
    toDate = DateField('To Date', format='%Y-%m-%d')

    merchant = StringField('Merchant')
    acquirer = StringField('Acquirer')
    submit = SubmitField('Process')


class TransactionQueryForm(ReportForm):

    status = StringField('Status')
    operation = StringField('Operation')

    payment_method = StringField('Operation')
    error_code = StringField('Operation')
    filter_field = StringField('Operation')
    filter_value = StringField('Operation')
    page = StringField('Page')

    submit = SubmitField('Process')