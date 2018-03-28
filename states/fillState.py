from .state import State
from .station import Station

class FillState(State):
    def __init__(self):
        super(FillState, self).__init__()
        self._station = Station.get()
        self._station.pump.on()
        self._credit = self._station.user.getCredit()
        self._charge = 0
        self._station.screen.showFill()

        self._station.screen.setDriver(self._station.user.getDriverDict())
        self._station.screen.setVehicle(self._station.user.getVehicleDict())
        self._station.screen.setLiters(self._credit)

    def onFlowMeterChange(self, value):
        self._charge = value
        if self._charge >= self._credit-1:
            self._station.pump.off()
        return self

    def onRfidEMRead(self, rfid):
        return self.onPumpCloses()

    def onPumpCloses(self):
        self._station.pump.off()
        self._station.user.addCharge(self._charge)
        print("RESET")
        self._station.flowMeter.reset()
        self._station.rfid_em.off()
        self._station.user = None
        from .vehicleinState import VehicleinState
        return VehicleinState()
