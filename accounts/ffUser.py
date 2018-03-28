from .user import User
from time import time
import http.client

class FfUser(User):
    def __init__(self, userId, data, rfidlr, rfidem):
        super(FfUser, self).__init__()
        self._userId  = userId
        self._data = data
        self._rfidlr = rfidlr
        self._rfidem = rfidem
        self._url = 'us-central1-petromatic-4240b.cloudfunctions.net'

        if "order" in data and len(data["order"]) > 0:
            self._limit = next (iter (data["order"].values()))["value"]
        else:
            self._limit = 0

    def getCredit(self):
        return self._limit

    def getVehicleDict(self):
        return self._data["truck_data"]

    def getDriverDict(self):
        return self._data["driver_data"]

    def addCharge(self, charge):
        localtime = int(time()*1000)
        key = ""
        for k in self._data["order"]:
            key = k
            break
        
        conn = http.client.HTTPSConnection(self._url)
        conn.request("GET", "/pushTransaction/"+"/".join([self._rfidlr, self._rfidem, key, str(charge)]))
        res = conn.getresponse()
        data = res.read()
