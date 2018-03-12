#!/usr/bin/env python3
from serial import Serial
from devices.GPIORelay import GPIORelay
from devices.flowMeter import FlowMeter
from devices.rfid_em import RfidEM
from devices.screen.screen import Screen

from accounts.ffAccountManager import FfAccountManager

from states.station import Station
from states.stateMachine import StateMachine


def main():
    s = StateMachine()
    station = Station.get()
    station.pump = GPIORelay(21)
    station.flowMeter = FlowMeter(Serial('/dev/ttyUSB0', timeout=10))
    station.flowMeter.suscribe(lambda e,a: s.do(e,a))
    station.rfid_em = RfidEM(Serial('/dev/ttyUSB2', timeout=1))
    station.rfid_em.suscribe(lambda e,a: s.do(e,a))
    station.screen = Screen()
    station.screen.run()

def testAccount():
    a = FfAccountManager()
    u = a.getUserByRFID("AhPg","0000863362")
    credit = u.getCredit()
    print("Credit: "+str(credit))
    u.addCharge(credit/2)

if __name__ == "__main__":
    main()
    # testAccount()
