"""
    RFID
"""
from threading import Thread
from time import sleep
from threading import Lock
import re

class RfidEM(Thread):
    """
        RFID class
    """
    def __init__(self, serial):
        super(RfidEM, self).__init__()
        self.serial = serial
        self.serialLock = Lock()
        self.daemon = True
        self.eventListeners = []
        self.start()

    def suscribe(self, listener):
        """Suscribe to events"""
        self.eventListeners += [listener]

    def reset(self):
        self.serialLock.acquire()
        self.serial.write(b'R')
        self.serialLock.release()

    def setColor(self,r,g,b):
        msg = 'BD{0:03}{1:03}{2:03}F.'.format(r/255,g/255,b/255).encode()
        self.serialLock.acquire()
        self.serial.write(msg)
        self.serialLock.release()

    def off(self):
        self.serialLock.acquire()
        self.serial.write(b'FB.')
        self.serialLock.release()

    def on(self):
        self.serialLock.acquire()
        self.serial.write(b'FA.')
        self.serialLock.release()

    def ack(self):
        self.serialLock.acquire()
        self.serial.write(b'DB.')
        self.serialLock.release()

    def nack(self):
        self.serialLock.acquire()
        self.serial.write(b'DC.')
        self.serialLock.release()

    def run(self):
        exp = re.compile('>SIC [0-9]{10}<')
        while True:
            self.serialLock.acquire()
            data = self.serial.readline()
            self.serialLock.release()
            if exp.match(data) is not None:
                rfid = data[r.pos+5:r.pos+13]
                self.raiseEvent("RfidEMRead",[rfid])
            sleep(0.125)
    
    def raiseEvent(self, event, args):
        for listener in self.eventListeners:
            listener(event, args)