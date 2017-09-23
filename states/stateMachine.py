from .idleState import IdleState

class StateMachine(object):
    def __init__(self):
        self.state = IdleState()
    
    def do(self, event, args):
        print("DO "+event)
        print(type(self.state))
        self.state = self.state.do(event, args)
        print(type(self.state))