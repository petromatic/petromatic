from .state import State

class CloseExitGateState(State):
    def __init__(self):
        super(CloseExitGateState, self).__init__()

    def onExitBarrierCloses(self):
        print(__file__ + " TODO: Reopen exit gate")
        from .exitState import ExitState
        return ExitState()

    def onExitGateCloses(self):
        from .idleState import IdleState
        return IdleState()
