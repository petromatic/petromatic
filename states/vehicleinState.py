from .state import State

class VehicleinState(State):
    def __init__(self):
        super(VehicleinState, self).__init__()

    def onPumpAccessRequest(self):
        from .fillState import FillState
        return FillState()

    def onExitRequest(self):
        print(__file__ + " TODO: Open exit gate")
        from .exitState import ExitState
        return ExitState()
