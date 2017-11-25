
class Station(object):
    instance = None

    def __init__(self):
        self.pump = None
        self.flowMeter = None
        self.rfid_em = None

    @staticmethod
    def get():
        if Station.instance is None:
            Station.instance = Station()
        return Station.instance
    