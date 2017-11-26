
class User(object):
    def __init__(self):
        super(User, self).__init__()
        self._credit = 0

    def getCredit(self):
        return self._credit

    def addCharge(self, charge):
        self._credit -= charge