from .state import State

class VehicleinState(State):
    def __init__(self):
        super(VehicleinState, self).__init__()

    def do(self, event, args):
        super(VehicleinState, self).do(event, args)
        if event == "PumpAccessRequest":
            return self.onPumpAccessRequest()
        if event == "ExitRequest":
            return self.onExitRequest()
        else:
            return self

    def onPumpAccessRequest(self):
        print(__file__ + " TODO: Start pump")
        from .fillState import FillState
        return FillState()

    def onExitRequest(self):
        print(__file__ + " TODO: Open exit gate")
        from .exitState import ExitState
        return ExitState()
