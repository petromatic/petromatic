"""
    FlowMeter
"""
from threading import Thread
from time import sleep

class FlowMeter(Thread):
    """
        FlowMeter class
    """
    def __init__(self, serial):
        super(FlowMeter, self).__init__()
        self.serial = serial
        self.daemon = True
        self.eventListeners = []
        self.start()

    def suscribe(self, listener):
        """Suscribe to events"""
        self.eventListeners += [listener]

    def run(self):
        v0 = 0.0
        while True:
            self.serial.write(b'FM+ACM\r\n')
            v = float(self.serial.readline()) # Needs timeout in serial for security
            if v != v0:
                self.raiseEvent("FlowMeterChange",[v])
            v0 = v
            sleep(0.125)
    
    def raiseEvent(self, event, args):
        for listener in self.eventListeners:
            listener(event, args)