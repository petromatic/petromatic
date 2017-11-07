from socket import socket, AF_INET, SOCK_STREAM

class RemoteRelay(object):
    def __init__(self, ip, port, pin):
        """
            Creates a remote relay instance
        """
        self.ip = ip
        self.port = port
        self.pin = pin

    def set(self, state):
        """
            Sets relay state:
                0: Off
                1: On
        """
        with socket(AF_INET, SOCK_STREAM) as sock:
            sock.connect((self.ip, self.port))
            sock.sendall("O"+self.pin+state)