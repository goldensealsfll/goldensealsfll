# LEGO type:standard slot:3 autostart

from spike import ColorSensor, MotorPair, Motor, PrimeHub
from spike.control import Timer

hub = PrimeHub()
color = ColorSensor('A')
wheels = MotorPair('F', 'B')
updown = Motor('E')
sideside = Motor('C')
timer = Timer() 