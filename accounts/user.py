
class User(object):
    def __init__(self):
        super(User, self).__init__()
        self._credit = 0
        self._vehicle = {}
        self._driver = {}
        self._invoiceId = 0

    def getCredit(self):
        return self._credit

    def addCharge(self, charge):
        self._credit -= charge

    def getVehicleDict(self):
        return self._vehicle

    def getDriverDict(self):
        return self._driver

    def getInvoiceId(self):
        return self._invoiceId