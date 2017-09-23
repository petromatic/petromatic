from .state import State

class CloseExitGateState(State):
    def __init__(self):
        super(CloseExitGateState, self).__init__()

    def do(self, event, args):
        super(CloseExitGateState, self).do(event, args)
        if event == "ExitBarrierOpens":
            return self.onExitBarrierCloses()
        if event == "ExitGateCloses":
            return self.onExitGateCloses()
        else:
            return self

    def onExitBarrierCloses(self):
        print(__file__ + " TODO: Reopen exit gate")
        from .exitState import ExitState
        return ExitState()

    def onExitGateCloses(self):
        from .idleState import IdleState
        return IdleState()
