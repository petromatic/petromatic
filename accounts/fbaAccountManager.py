from .accountManager import AccountManager
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
from .fbaUser import FbaUser


class FbaAccountManager(AccountManager):
    def __init__(self):
        super(FbaAccountManager, self).__init__()
        self._url = 'https://petromatic-4240b.firebaseio.com'
        self._cred = credentials.Certificate('keys/admin.json')
        self._tid = '797647ef89c8ddb64d382bc4c87e980de7328fb8'

    def getUserByRFID(self, rfidlr, rfidem):
        app = firebase_admin.initialize_app(self._cred, {'databaseURL': self._url, 'databaseAuthVariableOverride': {'rfidlr': rfidlr,'rfidem': rfidem, 'tid': self._tid}})
        userId = db.reference('rfid').child(rfidlr).child(rfidem).get()
        return FbaUser(userId = userId)
