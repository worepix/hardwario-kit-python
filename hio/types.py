class Sensor:
    def __init__(self, interface):
        self._interface = interface
        self._init()

    def read(self):
        return self._read()

    def set_unit(self, unit):
        self._unit = unit