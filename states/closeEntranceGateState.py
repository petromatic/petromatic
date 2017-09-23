from .state import State

class CloseEntranceGateState(State):
    def __init__(self):
        super(CloseEntranceGateState, self).__init__()

    def do(self, event, args):
        super(CloseEntranceGateState, self).do(event, args)
        if event == "EntranceBarrierOpens":
            return self.onEntranceBarrierCloses()
        if event == "EntranceGateCloses":
            return self.onEntranceGateCloses()
        else:
            return self

    def onEntranceBarrierCloses(self):
        print(__file__ + " TODO: Reopen entrance gate")
        from .enterState import EnterState
        return EnterState()

    def onEntranceGateCloses(self):
        from .vehicleinState import VehicleinState
        return VehicleinState()
        