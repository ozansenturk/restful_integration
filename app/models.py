from app import db
from datetime import datetime


class Token():

    def __init__(self, token, status):
        self.token = token  # instance variable unique to each instance
        self.status = status  # instance variable unique to each instance

    def __repr__(self):
        return '<Token composed of  token: {}, status: {}' \
            .format(self.token, self.status)

class Report():

    def __init__(self, count, total, currency):
        self.count = count
        self.total = total
        self.currency = currency

    def __repr__(self):
        return '<Report composed of count: {}, total: {}, currency: {}' \
            .format(self.count, self.total, self.currency)