#!/usr/bin/env python3

from serial import Serial
from devices.GPIORelay import GPIORelay
from devices.flowMeter import FlowMeter
from devices.rfid_em import RfidEM
from devices.rfid_lr import RfidLR
from devices.screen.screen import Screen

from accounts.ffAccountManager import FfAccountManager

from states.station import Station
from states.stateMachine import StateMachine
import configparser

from subprocess import check_output

def main():
    config = configparser.SafeConfigParser()
    config.read('config.ini')
    station = Station.get()
    gpioRelay = int(config.get('PUMP','RELAY_PIN', fallback=21))

    flowMeterDev = config.get('FLOWMETER', 'DEV')
    rfidemDev = config.get('RFIDEM', 'DEV')
    rfidlrDev = config.get('RFIDLR', 'DEV')

    flowMeterPort = "/dev/"+check_output("./usb.sh "+flowMeterDev, shell=True).decode('utf-8').strip()
    rfidemPort    = "/dev/"+check_output("./usb.sh "+rfidemDev, shell=True).decode('utf-8').strip()
    rfidlrPort    = "/dev/"+check_output("./usb.sh "+rfidlrDev, shell=True).decode('utf-8').strip()

    station.pump = GPIORelay(gpioRelay)
    station.flowMeter = FlowMeter(Serial(flowMeterPort, timeout=1))
    station.flowMeter.suscribe(lambda e,a: s.do(e,a))
    station.rfid_em = RfidEM(Serial(rfidemPort, timeout=1))
    station.rfid_em.suscribe(lambda e,a: s.do(e,a))
    station.rfid_lr = RfidLR(Serial(rfidlrPort, timeout=1))
    station.rfid_lr.suscribe(lambda e,a: s.do(e,a))
    station.screen = Screen()
    station.accountManager = FfAccountManager()
    s = StateMachine()
    station.screen.run()

if __name__ == "__main__":
    main()
