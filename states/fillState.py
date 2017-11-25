from .state import State
from .station import Station

class FillState(State):
    def __init__(self):
        super(FillState, self).__init__()
        self.station = Station.get()
        self.station.pump.on()
        self.charge = 5

    def onChargeChange(self, charge):
        self.charge = int(charge)
        return self

    def onFlowMeterChange(self, value):
        if value > self.charge:
            self.station.pump.off()
        return self

    def onPumpCloses(self):
        self.station.pump.off()
        self.station.flowMeter.reset()
        self.station.rfid_em.off()
        from .vehicleinState import VehicleinState
        return VehicleinState()
