from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from ..observable import Observable

class Driver(object):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.dni = ""
    
    def setName(name):
        self.name = name
    
    def setDNI(dni):
        self.dni = dni

class Vehicle(object):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.plate = ""
    
    def setName(name):
        self.name = name
    
    def setPlate(plate):
        self.plate = plate

class FillWindow(GridLayout, Observable):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.eventListeners = []
        self.driver = Driver()
        self.vehicle = Vehicle()
        self.liters = 0

    def setVehicle(self, vehicle):
        self.vehicle = vehicle

    def setDriver(self, driver):
        self.driver = driver

    def setLiters(self, liters):
        self.liters = liters

    def clicked(self):
        self.raiseEvent("ExitButtonClick",[])

class Screen(App, Observable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def setDriver(self, driver):
        self.win.setDriver(driver)

    def setVehicle(self, vehicle):
        self.win.setVehicle(vehicle)
    
    def setLiters(self, liters):
        self.win.setLiters(self, liters)

    def build(self):
        self.win = Builder.load_file("FillWindow.kv")
        self.win.suscribe(self.raiseEvent)
        return self.win

if __name__ == '__main__':
    Screen().run()