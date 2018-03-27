from .accountManager import AccountManager
from .ffUser import FfUser
import http.client
import json

class FfAccountManager(AccountManager):
    def __init__(self):
        super(FfAccountManager, self).__init__()
        # self._url = 'petromatic-4240b.firebaseio.com'
        self._url = 'us-central1-petromatic-4240b.cloudfunctions.net'
        # self._url = 'localhost'
        self._tid = '797647ef89c8ddb64d382bc4c87e980de7328fb8'

    def RfidLRIsValid(self, rfid):
        return True

    def getUserByRFID(self, rfidlr, rfidem):
        conn = http.client.HTTPSConnection(self._url)
        #conn = http.client.HTTPConnection(self._url, 5000)
        print(self._url +"/validateDriver/"+"/".join([rfidlr, rfidem]))
        conn.request("GET", "/validateDriver/"+"/".join([rfidlr, rfidem]))
        res = conn.getresponse()
        data = res.read()
        print(data)
        data = json.loads(data.decode())
        userId = data["user"]
        return FfUser(userId = userId, data = data, rfidlr = rfidlr, rfidem = rfidem)
