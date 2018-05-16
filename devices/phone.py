"""
    Phone
"""
from threading import Thread
from time import sleep
from .observable import Observable
from threading import Lock
import json

class FlowMeter(Thread, Observable):
    """
        Phone class
    """
    def __init__(self, serial):
        super().__init__()
        self.serial = serial
        self.daemon = True
        self.serialLock = Lock()
        self.start()

    def run(self):
        while True:
            self.serialLock.acquire()
            data = self.serial.readline() # Needs timeout in serial for security
            self.serialLock.release()
            if len(data)>0:
                try:
                    mensaje = json.loads(data)
                    invoiceId = mensaje["invoiceId"]
                    driver = mensaje["driver"]
                    vehicle = mensaje["plate"]
                    liters = mensaje["liters"]
                    self.raiseEvent("PhoneRequestCharge",[invoiceId, driver, vehicle, liters])
                except:
                    pass
            sleep(0.1)
