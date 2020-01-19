from ..types import Sensor
from .. import actions
from microbit import *

i2c.init(freq=100000, sda=pin20, scl=pin19)

class Tmp112(Sensor):
    UNIT_FAHRENHEIT = 0
    UNIT_CELSIUS = 1

    def _read(self):
        return i2c.read(72, 2, repeat=False)

    def _init(self):
        i2c.write(72, b'\x01\x81', repeat=False)
        i2c.write(72, 0x00, repeat=False)