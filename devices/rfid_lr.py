"""
    RFID
"""
from threading import Thread
from time import sleep
from threading import Lock
import base64
from observable import Observable

class RfidLR(Thread, Observable):
    """
        Long Range RFID class
    """
    def __init__(self, serial):
        super().__init__()
        self.serial = serial
        self.serialLock = Lock()
        self.daemon = True
        self.eventListeners = []
        self.start()

    def run(self):
        while True:
            self.serialLock.acquire()
            data = self.serial.readline()
            self.serialLock.release()
            if len(data) > 0:
                self.raiseEvent("RfidLRRead",[base64.b64encode(data)])
            sleep(0.125)
