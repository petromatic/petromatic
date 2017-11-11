from socket import socket, AF_INET, SOCK_STREAM

class RemoteRelay(object):
    def __init__(self, ip, port, pin):
        """
            Creates a remote relay instance
        """
        self.ip = ip
        self.port = port
        self.pin = pin
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.connect((self.ip, self.port))

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
        msg = "O"+str(self.pin)+str(state)
        self.sock.send(msg.encode('ascii'))
