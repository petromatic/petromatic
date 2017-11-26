from .user import User
from firebase_admin import db
from time import time

class FbaUser(User):
    def __init__(self, userId):
        super(FbaUser, self).__init__()
        self._userRef = db.reference('users').child(userId)
        self._transactionRef = db.reference('user_transactions').child(userId)
        self._credit = self._userRef.child("credit").get()
        start = self._credit['updated']
        transactions = self._transactionRef.order_by_child('timestamp').start_at(start).get()
        for key in transactions:
            self._credit["value"]+=transactions[key]["value"]

    def getCredit(self):
        return self._credit["value"]

    def addCharge(self, charge):
        self._credit["value"] -= charge
        self._transactionRef.push({"localtime":int(time()),"value":-charge,"timestamp":{".sv": "timestamp"}})
