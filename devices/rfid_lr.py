"""
    RFID
"""
from threading import Thread
from time import sleep
from threading import Lock
import base64

class RfidLR(Thread):
    """
        Long Range RFID class
    """
    def __init__(self, serial):
        super(RfidLR, self).__init__()
        self.serial = serial
        self.serialLock = Lock()
        self.daemon = True
        self.eventListeners = []
        self.start()

    def suscribe(self, listener):
        """Suscribe to events"""
        self.eventListeners += [listener]

    def run(self):
        while True:
            self.serialLock.acquire()
            data = self.serial.readline()
            self.serialLock.release()
            if len(data) > 0:
                self.raiseEvent("RfidLRRead",[base64.b64encode(data)])
            sleep(0.125)
    
    def raiseEvent(self, event, args):
        for listener in self.eventListeners:
            listener(event, args)