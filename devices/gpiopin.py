import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class GPIOPin(object):
    def __init__(self, pin):
        super().__init__()
        self._pin = pin
        GPIO.setup(self._pin, GPIO.OUT)
        
    def setValue(self, value):
        GPIO.output(self._pin, value)

def cleanup():
    GPIO.cleanup()

import atexit
atexit.register(cleanup)