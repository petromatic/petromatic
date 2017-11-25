from .state import State
from .station import Station

class VehicleinState(State):
    def __init__(self):
        super(VehicleinState, self).__init__()
        self.station = Station.get()
        self.station.rfid_em.on()

    def onRfidEMRead(self, rfid):
        from .fillState import FillState
        self.station.rfid_em.ack()
        return FillState()

    def onPumpAccessRequest(self):
        from .fillState import FillState
        return FillState()

    def onExitRequest(self):
        print(__file__ + " TODO: Open exit gate")
        self.station.rfid_em.off()
        from .exitState import ExitState
        return ExitState()
