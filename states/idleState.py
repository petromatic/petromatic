from .state import State

class IdleState(State):
    def __init__(self):
        super(IdleState, self).__init__()

    def onAccessRequest(self):
        print(__file__ + " TODO: Open entrance gate")
        print(__file__ + " TODO: Power on")
        from .enterState import EnterState
        return EnterState()