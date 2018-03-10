from .state import State
from .station import Station

class IdleState(State):
    def __init__(self):
        super(IdleState, self).__init__()
        self._station = Station.get()

    def onAccessRequest(self):
        print(__file__ + " TODO: Power on")
        from .enterState import EnterState
        self._station.rflrId = "AhPg"
        return EnterState()
        
    def onRfidLRRead(self, rfid):
        print(__file__ + " TODO: Power on")
        from .vehicleinState import VehicleinState
        if self._station.accountManager.RfidLRIsValid(rfid):
            self._station.rflrId = rfid
            return VehicleinState()
        else:
            return self

