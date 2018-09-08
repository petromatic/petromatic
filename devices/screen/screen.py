from kivy.app import App
from kivy.properties import NumericProperty, DictProperty
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, NoTransition, Screen as kvScreen
from ..observable import Observable
import os

class FillWindow(kvScreen, Observable):
    liters = NumericProperty(0.0)
    driver = DictProperty({'name' : "",'dni' : ""})
    vehicle = DictProperty({'name' : "",'plate' : ""})

    def __init__(self, *args, **kwargs):
        super().__init__(name="fill",**kwargs)
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
        super().__init__(name="idle",**kwargs)
        
class Screen(App, Observable):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = ScreenManager(transition=NoTransition())
        path = os.path.dirname(os.path.abspath(__file__))
        self.idle = Builder.load_file(os.path.join(path,"idleWindow.kv"), name="idle")
        self.fill = Builder.load_file(os.path.join(path,"fillWindow.kv"), name="fill")
        self.fill.suscribe(self.raiseEvent)
        self.sm.add_widget(self.fill)
        self.sm.add_widget(self.idle)
            
    def setDriver(self, driver):
        self.fill.setDriver(driver)

    def setVehicle(self, vehicle):
        self.fill.setVehicle(vehicle)
    
    def setLiters(self, liters):
        self.fill.setLiters(liters)

    def showFill(self):
        self.sm.current = "fill"

    def showIdle(self):
        self.sm.current = "idle"

    def build(self):
        return self.sm

if __name__ == '__main__':
    Screen().run()
