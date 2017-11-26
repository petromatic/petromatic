from .state import State
from .station import Station

class IdleState(State):
    def __init__(self):
        super(IdleState, self).__init__()
        self._station = Station.get()

    def RfidLRRead(self, rfid):
        print(__file__ + " TODO: Open entrance gate")
        print(__file__ + " TODO: Power on")
        from .enterState import EnterState
        if self._station.accountManager.RfidLRIsValid(rfid):
            self._station.rflrId = rfid
            return EnterState()
        else:
            return self