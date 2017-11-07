from .state import State

class CloseEntranceGateState(State):
    def __init__(self):
        super(CloseEntranceGateState, self).__init__()

    def onEntranceBarrierCloses(self):
        print(__file__ + " TODO: Reopen entrance gate")
        from .enterState import EnterState
        return EnterState()

    def onEntranceGateCloses(self):
        from .vehicleinState import VehicleinState
        return VehicleinState()
        