from .state import State
from .station import Station

class VehicleinState(State):
    def __init__(self):
        super(VehicleinState, self).__init__()
        self._station = Station.get()
        self._station.rfid_em.on()

    def onRfidEMRead(self, rfid):
        from .fillState import FillState
        user = self._station.accountManager.getUserByRFID(self._station., rfid)
        if user is not None:
            self._station.user = user
            self._station.rfid_em.ack()
            return FillState()
        else:
            self._station.rfid_em.nack()
            return self

    def onPumpAccessRequest(self):
        from .fillState import FillState
        return FillState()

    def onExitRequest(self):
        print(__file__ + " TODO: Open exit gate")
        self._station.rfid_em.off()
        self._station.rflrId = None
        from .exitState import ExitState
        return ExitState()
