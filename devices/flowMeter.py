"""
    FlowMeter
"""
from threading import Thread
from time import sleep
from .observable import Observable
from threading import Lock

class FlowMeter(Thread, Observable):
    """
        FlowMeter class
    """
    def __init__(self, serial):
        super().__init__()
        self.serial = serial
        self.daemon = True
        self.serialLock = Lock()
        self.start()

    def reset(self):
        self.serialLock.acquire()
        self.serial.write(b'FM+RST.ACM\n')
        self.serialLock.release()

    def print(self):
        '''
        Prints lines

        :return: Ticket number
        :rtype: Int
        '''
        self.serialLock.acquire()
        self.serial.write(b'FM+PTR\n')
        data = self.serial.readline()
        self.serialLock.release()
        return int(data.strip())

    def setLabel(self, position, value):
        '''
        Sets printer label

        :param int position: The position of the label in the ticket.
        :param str value: The text to be printed. Must be less than 24 chars.
        :return: Ticket label changed
        :rtype: str
        '''
        self.serialLock.acquire()
        self.serial.write('FM+LAB{0}={1}\n'.format(position, value).encode())
        data = self.serial.readline()
        self.serialLock.release()
        return data

    def run(self):
        v0 = 0.0
        while True:
            self.serialLock.acquire()
            self.serial.write(b'FM+ACM\n')
            data = self.serial.readline()
            self.serialLock.release()
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
