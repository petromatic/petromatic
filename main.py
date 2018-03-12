#!/usr/bin/env python3

from serial import Serial
from devices.GPIORelay import GPIORelay
from devices.flowMeter import FlowMeter
from devices.rfid_em import RfidEM
from devices.screen.screen import Screen

from accounts.ffAccountManager import FfAccountManager

from states.station import Station
from states.stateMachine import StateMachine
import configparser


def main():
    config = configparser.SafeConfigParser()
    config.read('config.ini')
    s = StateMachine()
    station = Station.get()
    gpioRelay = int(config.get('PUMP','RELAY_PIN', fallback=21))
    flowMeterPort = config.get('FLOWMETER', 'TTY', fallback='/dev/ttyUSB0')
    rfidemPort = config.get('RFIDEM', 'TTY', fallback='/dev/ttyUSB1')
    rfidlrPort = config.get('RFIDLR', 'TTY', fallback='/dev/ttyUSB2')
    station.pump = GPIORelay(gpioRelay)
    station.flowMeter = FlowMeter(Serial(flowMeterPort, timeout=1))
    station.flowMeter.suscribe(lambda e,a: s.do(e,a))
    station.rfid_em = RfidEM(Serial(rfidemPort, timeout=1))
    station.rfid_em.suscribe(lambda e,a: s.do(e,a))
    station.rfid_lr = RfidEM(Serial(rfidlrPort, timeout=1))
    station.rfid_lr.suscribe(lambda e,a: s.do(e,a))
    station.screen = Screen()
    station.screen.run()

if __name__ == "__main__":
    main()
