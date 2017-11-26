from .state import State
from .station import Station

class FillState(State):
    def __init__(self):
        super(FillState, self).__init__()
        self._station = Station.get()
        self._station.pump.on()
        self._credit = self._station.user.getCredit()
        self._charge = 0

    def onFlowMeterChange(self, value):
        self._charge = value
        if self._charge >= self._credit-1:
            self._station.pump.off()
        return self

    def onPumpCloses(self):
        self._station.pump.off()
        self._station.user.addCharge(self._charge)
        self._station.flowMeter.reset()
        self._station.rfid_em.off()
        self._station.user = None
        from .vehicleinState import VehicleinState
        return VehicleinState()
