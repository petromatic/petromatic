from .state import State

class EnterState(State):
    def __init__(self):
        super(EnterState, self).__init__()

    def onEntranceBarrierCloses(self):
        print(__file__ + " TODO: Close entrance gate")
        from .closeEntranceGateState import CloseEntranceGateState
        return CloseEntranceGateState()