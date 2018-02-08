from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class Driver(object):
    def __init__(self):
        super(Driver, self).__init__()
        self.name = "Nicolás Dazeo"
        self.dni = "36383780"

class Vehicle(object):
    def __init__(self):
        super(Vehicle, self).__init__()
        self.name = "Ford Cargo 916"
        self.plate = "EFN 573"

class ControlWindow(GridLayout):
    def __init__(self, *args, **kwargs):
        super(ControlWindow, self).__init__(**kwargs)
        self.eventListeners = []
        self.driver = Driver()
        self.vehicle = Vehicle()
        
    def clicked(self):
        self.raiseEvent("ExitButton",[])

    def raiseEvent(self, event, args):
        for listener in self.eventListeners:
            listener(event, args)

    def suscribe(self, listener):
        """Suscribe to events"""
        self.eventListeners += [listener]

class Screen(object):
    def __init__(self):
        super(Screen, self).__init__()
        KvApp().run()

class KvApp(App):
    def __init__(self, **kwargs):
        super(KvApp, self).__init__(**kwargs)

    def build(self):
        win = Builder.load_file("screen.kv")
        win.suscribe(self.event)
        return win
    
    def event(self, name, args):
        print("event: "+name)

if __name__ == '__main__':
    KvApp().run()