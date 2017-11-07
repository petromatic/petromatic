from .state import State

class FillState(State):
    def __init__(self):
        super(FillState, self).__init__()

    def onPumpCloses(self):
        print(__file__ + " TODO: Turn pump off")
        from .vehicleinState import VehicleinState
        return VehicleinState()
