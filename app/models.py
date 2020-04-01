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


class Merchant():

    def __init__(self, referenceNo, status, customData, type,
                 operation, message, created_at, transactionId):
        self.referenceNo = referenceNo
        self.status = status
        self.customData = customData
        self.type = type
        self.operation = operation
        self.created_at = created_at
        self.message = message
        self.transactionId = transactionId


    def __repr__(self):
        return '<Merchant composed of reference_no: {}, status: {}, customData: {}, ' \
               'type: {}, operation: {}, ' \
               'message: {}, created_at: {}, ' \
               'transaction_id: {}' \
            .format(self.referenceNo, self.status, self.customData, self.type,
                    self.operation, self.message, self.created_at,
                    self.transactionId)


class Acquirer(MerchantBase):

    def __init__(self, id, name, code, type):
        super().__init__(id, name)
        self.code = code
        self.type = type

    def __repr__(self):
        return '<Acquirer composed of code: {}, type: {}' \
            .format(self.code, self.type)


class CustomerInfoBase:
    def __init__(self, number, email, billingFirstName, billingLastName):
        self.number = number
        self.email = email
        self.billingFirstName = billingFirstName
        self.billingLastName = billingLastName

    def __repr__(self):
        return '<CustomerInfoBase composed of number: {}, email: {}, ' \
               'billingFirstName: {}, billingLastName: {}, '\
            .format(self.number, self.email, self.billingFirstName, self.billingLastName)


class FxMerchant:
    def __init__(self, originalAmount, originalCurrency, convertedAmount, convertedCurrency):
        self.originalAmount = originalAmount
        self.originalCurrency = originalCurrency
        self.convertedAmount = convertedAmount
        self.convertedCurrency = convertedCurrency

    def __repr__(self):
        return '<MerchantBase composed of original_amount: {}, original_currency: {}' \
            .format(self.originalAmount, self.originalCurrency,
                    self.convertedAmount, self.convertedCurrency)


class TransactionQuery:

    def __init__(self, *initial_data, **kwargs):
        for dictionary in initial_data:
            if 'customerInfo' in dictionary:

                customer_info = dictionary['customerInfo']
                # TODO data not consistent

                if 'number' in customer_info and 'email' in customer_info:
                    cust = CustomerInfoBase(**customer_info)
                    self.CustomerInfoBase = cust
                else:
                    self.CustomerInfoBase = CustomerInfoBase(None, None, None, None)
            else:
                self.CustomerInfoBase = CustomerInfoBase(None, None, None, None)

            if 'fx' in dictionary:
                fx = dictionary['fx']['merchant']
                fx_merchant = FxMerchant(**fx)
                self.FxMerchant = fx_merchant

            if 'acquirer' in dictionary:
                acquirer = dictionary['acquirer']
                acq = Acquirer(acquirer['id'], acquirer['name'], acquirer['code'], acquirer['type'])
                self.Acquirer = acq
            else:
                self.Acquirer = Acquirer(None, None, None, None)

            if 'merchant' in dictionary:
                merchant = dictionary['merchant']
                merc = MerchantBase(merchant['id'], merchant['name'])
                self.MerchantBase = merc

            if 'transaction' in dictionary:
                transaction = dictionary['transaction']["merchant"]
                trans = Merchant(**transaction)
                self.Merchant = trans

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __repr__(self):
        return str(self.__dict__)