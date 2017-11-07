#!/usr/bin/env python3

from devices.httpDevice import httpDevice
from states.stateMachine import StateMachine

#h = httpDevice(8080)
#s = StateMachine()
#h.suscribe(lambda e,a: s.do(e,a))

from serial import Serial

ser = Serial('/dev/ttyACM0')
from devices.flowMeter import FlowMeter

f = FlowMeter(ser)
f.suscribe(lambda e,a: print(e,a))

h = httpDevice(8080)
s = StateMachine()
h.suscribe(lambda e,a: s.do(e,a))
