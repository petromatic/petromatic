
class State(object):
    def __init__(self):
        pass

    def do(self, event, args):
        handler = getattr(self, "on"+event, None)
        if callable(handler):
            return handler(*args)
        else:
            return self
