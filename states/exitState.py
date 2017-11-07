from .state import State
from .closeExitGateState import CloseExitGateState

class ExitState(State):
    def __init__(self):
        super(ExitState, self).__init__()

    def onExitBarrierCloses(self):
        print(__file__ + " TODO: Close exit gate")
        return CloseExitGateState()
