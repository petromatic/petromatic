from threading import Thread
from time import sleep

class FlowMeter(Thread):
    def __init__(self, serial):
        super(FlowMeter, self).__init__()
        self.serial = serial
        self.daemon = True
        self.start()

    def run(self):
        v0 = 0.0
        while True:
            self.serial.write(b'')
            v = float(ser.readline()) # Needs timeout in serial for security
            if v != v0:
                raiseEvent("FlowMeterChange",[v])
            v0 = v
            sleep(0.125)
    
    def raiseEvent(self, event, args):
        for listener in self.eventListeners:
            listener(event, args)