
class Station(object):
    instance = None

    def __init__(self):
        self.pump = None
        self.flowMeter = None
        self.rfid_em = None
        self.rfid_lr = None
        self.accountManager = None
        self.user = None
        self.rflrId = None

    @staticmethod
    def get():
        if Station.instance is None:
            Station.instance = Station()
        return Station.instance
