from .state import State

class EnterState(State):
    def __init__(self):
        super(EnterState, self).__init__()

    def do(self, event, args):
        super(EnterState, self).do(event, args)
        if event == "EntranceBarrierCloses":
            return self.onEntranceBarrierCloses()
        else:
            return self

    def onEntranceBarrierCloses(self):
        print(__file__ + " TODO: Close entrance gate")
        from .closeEntranceGateState import CloseEntranceGateState
        return CloseEntranceGateState()