"""
    Printer
"""
from .observable import Observable
from threading import Lock

class Printer(Observable):
    """
        Printer class
    """
    def __init__(self, serial):
        super().__init__()
        self.serial = serial
        self.serialLock = Lock()

    def print(self, lines):
        '''
        Prints lines

        :param str[] lines: The person sending the message
        :return: None
        :rtype: None
        '''
        self.serialLock.acquire()
        for line in lines:
            self.serial.write("{0}\x0A\x0D".format(line).encode())
        self.serialLock.release()
