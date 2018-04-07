import sqlite3
from .accountManager import AccountManager
import os
from db import dict_factory
from .localUser import LocalUser

class LocalAccountManager(AccountManager):
    def __init__(self):
        super().__init__()
        path = os.path.dirname(os.path.abspath(__file__))
        self._connection = sqlite3.connect(os.path.join(path,'db.sqlite'))
        self._connection.row_factory = dict_factory

    def getUserByRFID(self, rfidlr, rfidem):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM user WHERE tagcamion = ? AND tagchofer = ?", rfidlr, rfidem)
        return LocalUser(cursor.fetchone(), self._connection)

    def RfidLRIsValid(self, rfidlr):
        cursor = self._connection.cursor()
        cursor.execute("SELECT 1 FROM user WHERE tagcamion = ?", rfidlr)
        result = cursor.fetchone()
        return result is not None