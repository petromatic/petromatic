from .state import State
from .closeExitGateState import CloseExitGateState

class ExitState(State):
    def __init__(self):
        super(ExitState, self).__init__()

    def do(self, event, args):
        super(ExitState, self).do(event, args)
        if event == "ExitBarrierCloses":
            return self.onExitBarrierCloses()
        else:
            return self

    def onExitBarrierCloses(self):
        print(__file__ + " TODO: Close exit gate")
        return CloseExitGateState()
