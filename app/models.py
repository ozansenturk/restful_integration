from app import db
from datetime import datetime


class Token():

    def __init__(self, token, status):
        self.token = token  # instance variable unique to each instance
        self.status = status  # instance variable unique to each instance

    def __repr__(self):
        return '<Token {} with token: {}, status: {}' \
            .format(self.token, self.status)