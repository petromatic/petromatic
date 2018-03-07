import RPi.GPIO as GPIO

class GPIOPin(Object):
    def __init__(self, pin):
        super().__init__()
        self._pin = pin
        GPIO.setup(self._pin, GPIO.OUT)

    def __enter__(self):
        GPIO.setmode(GPIO.BCM)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        GPIO.cleanup()

    def setValue(self, value):
        GPIO.output(self._pin, value)