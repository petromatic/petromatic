from socket import socket, AF_INET, SOCK_STREAM

class SimRelay(object):
    def __init__(self):
        """
            Creates a simulated relay instance
        """

    def off(self):
        self.set(0)

    def on(self):
        self.set(1)

    def set(self, state):
        """
            Sets relay state:
                0: Off
                1: On
        """
        print("State changed to {0}".format(state))