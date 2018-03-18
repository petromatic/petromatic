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
        # https://drive.google.com/file/u/0/d/1peIpY11eZ45KJWxPZpztpvczqKaRXnvH/view?usp=drive_web
        # 4.4. EPC(GEN 2) Identify Single Tag
        # HEAD ADDR(LSB) ADDR(MSB) CID1 RTN LENGTH AN D0 D1 D2 D3 D4 D5 D6 D7 D8 D9 D0 D1 CHKSUM
        # CC   FF        FF        10   00  0D     01 E2 00 34 11 B8 02 01 13 83 25 85 66 0xNN

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
