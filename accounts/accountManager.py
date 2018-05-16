from .user import User


class AccountManager(object):
    def __init__(self):
        super(AccountManager, self).__init__()

    def getUserByRFID(self, rfidlr, rfidem):
        pass

    def RfidLRIsValid(self, userId):
        pass

    def getUserFromDict(self, invoiceId, driver, vehicle, liters):
        user = User()
        user._invoiceId = invoiceId
        user._credit = liters
        user._driver = driver
        user._vehicle = vehicle
        return user