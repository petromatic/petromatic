
class Observable(object):
    def __init__(self):
        super(Observable, self).__init__()
        self.eventListeners = []
        
    def raiseEvent(self, event, args):
        for listener in self.eventListeners:
            listener(event, args)

    def suscribe(self, listener):
        self.eventListeners += [listener]
