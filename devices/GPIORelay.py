from .gpiopin import GPIOPin

class GPIORelay(GPIOPin):
    def __init__(self, pin):
        """
            Creates a GPIO relay instance
        """
        super().__init__(pin)

    def off(self):
        self.setValue(1)

    def on(self):
        self.setValue(0)
