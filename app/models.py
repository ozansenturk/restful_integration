from app import db
from datetime import datetime


class Token:

    def __init__(self, token, status):
        self.token = token  # instance variable unique to each instance
        self.status = status  # instance variable unique to each instance

    def __repr__(self):
        return '<Token composed of  token: {}, status: {}' \
            .format(self.token, self.status)

class Report:

    def __init__(self, count, total, currency):
        self.count = count
        self.total = total
        self.currency = currency

    def __repr__(self):
        return '<Report composed of count: {}, total: {}, currency: {}' \
            .format(self.count, self.total, self.currency)

class MerchantBase:
    def __init__(self, id, name):
        self.id = id
        self.name = name


    def __repr__(self):
        return '<MerchantBase composed of id: {}, name: {}' \
            .format(self.id, self.name)


class Merchant(MerchantBase):

    def __init__(self, reference_no, status, operation, message, created_at, transaction_id):

        self.reference_no = reference_no
        self.status = status
        self.operation = operation
        self.message = message
        self.created_at = created_at
        self.transaction_id = transaction_id
        self.message = message

    def __repr__(self):
        return '<Merchant composed of reference_no: {}, status: {}, operation: {}, message: {}, ' \
               'created_at: {}, transaction_id: {}, message: {}' \
            .format(self.reference_no, self.status, self.operation, self.message, self.created_at,
                    self.transaction_id, self.message)


class Acquirer(MerchantBase):

    def __init__(self, code, type):
        self.code = code
        self.type = type

    def __repr__(self):
        return '<Acquirer composed of code: {}, type: {}' \
            .format(self.code, self.type)


class CustomerInfoBase:
    def __init__(self, number, email, billing_first_name, billing_last_name):
        self.number = number
        self.email = email
        self.billing_first_name = billing_first_name
        self.billing_last_name = billing_last_name

    def __repr__(self):
        return '<CustomerInfoBase composed of number: {}, email: {}, ' \
               'billing_first_name: {}, billing_last_name: {}' \
            .format(self.number, self.email, self.billing_first_name, self.billing_last_name)


class FxMerchant:
    def __init__(self, original_amount, original_currency):
        self.original_amount = original_amount
        self.original_currency = original_currency

    def __repr__(self):
        return '<MerchantBase composed of original_amount: {}, original_currency: {}' \
            .format(self.original_amount, self.original_currency)


class TransactionQuery:

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            for key in dictionary:
                setattr(self, key, dictionary[key])
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __repr__(self):
        return str(self.__dict__)