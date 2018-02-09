"""
    FlowMeter
"""
from threading import Thread
from time import sleep
from observable import Observable

class FlowMeter(Thread, Observable):
    """
        FlowMeter class
    """
    def __init__(self, serial):
        super().__init__()
        self.serial = serial
        self.daemon = True
        self.eventListeners = []
        self.start()

    def reset(self):
        self.serial.write(b'FM+RST.ACM\n')

    def run(self):
        v0 = 0.0
        while True:
            self.serial.write(b'FM+ACM\n')
            data = self.serial.readline()
            if len(data)>0:
                try:
                    v = float(data.strip()) # Needs timeout in serial for security
                    if v != v0:
                        self.raiseEvent("FlowMeterChange",[v])
                        print(v)
                    v0 = v
                    sleep(0.1)
                except:
                    sleep(0.1)
                    pass
