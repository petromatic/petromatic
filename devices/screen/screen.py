from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, NoTransition, Screen as kvScreen
from ..observable import Observable
import os

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

class FillWindow(kvScreen, Observable):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
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

class IdleWindow(kvScreen, Observable):
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        
class Screen(App, Observable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
            
    def setDriver(self, driver):
        self.fill.setDriver(driver)

    def setVehicle(self, vehicle):
        self.fill.setVehicle(vehicle)
    
    def setLiters(self, liters):
        self.fill.setLiters(self, liters)

    def showFill(self):
        self.sm.switch_to("fill")

    def showIdle(self):
        self.sm.switch_to("idle")

    def build(self):
        path = os.path.dirname(os.path.abspath(__file__))
        self.idle = Builder.load_file(os.path.join(path,"IdleWindow.kv"), name="idle")
        self.fill = Builder.load_file(os.path.join(path,"fillWindow.kv"), name="fill")
        self.fill.suscribe(self.raiseEvent)
        self.sm = ScreenManager(transition=NoTransition())
        self.sm.add_widget(self.fill)
        self.sm.add_widget(self.idle)
        return self.sm

if __name__ == '__main__':
    Screen().run()
