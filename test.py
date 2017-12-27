#!/usr/bin/env python3
from serial import Serial
from devices.httpDevice import httpDevice
from devices.remoteRelay import RemoteRelay
from devices.flowMeter import FlowMeter
from devices.simRelay import SimRelay
from devices.rfid_em import RfidEM

from accounts.ffAccountManager import FfAccountManager

from states.station import Station
from states.stateMachine import StateMachine


def main():
    s = StateMachine()
    station = Station.get()
    station.pump = RemoteRelay("192.168.1.199",9760,1)
    #station.pump = SimRelay()
    station.flowMeter = FlowMeter(Serial('/dev/ttyUSB0', timeout=10))
    station.flowMeter.suscribe(lambda e,a: s.do(e,a))
    station.rfid_em = RfidEM(Serial('/dev/ttyUSB1', timeout=1))
    station.rfid_em.suscribe(lambda e,a: s.do(e,a))
    h = httpDevice(8080)
    h.suscribe(lambda e,a: s.do(e,a))
    station.accountManager = FfAccountManager()

def testAccount():
    a = FfAccountManager()
    u = a.getUserByRFID("AhPg","0000863362")
    credit = u.getCredit()
    print("Credit: "+str(credit))
    u.addCharge(credit/2)

if __name__ == "__main__":
    main()
    # testAccount()