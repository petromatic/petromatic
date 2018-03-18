"""
    RFID
"""
from threading import Thread
from time import sleep
from threading import Lock
import base64
from observable import Observable

def checksum(data):
    return bytes([((0xFF ^ (sum(bytearray(data)) % 0x100)) + 1)])

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
        msg = b'\x7C\xFF\xFF\x10\x32\x00'

        while True:
            self.serialLock.acquire()
            data = self.serial.readline()
            self.serialLock.release()
            if len(data) > 0:
                self.serialLock.acquire()
                self.serial.write(msg + checksum(msg))
                data = self.serial.readline()
                self.serialLock.release()
                self.raiseEvent("RfidLRRead",[base64.b64encode(data)])
            sleep(0.125)
