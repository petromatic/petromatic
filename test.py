#!/usr/bin/env python3

from devices.httpDevice import httpDevice
from states.stateMachine import StateMachine

h = httpDevice(8080)
s = StateMachine()
h.suscribe(lambda e,a: s.do(e,a))
