# LEGO type:standard slot:3 autostart

from spike import ColorSensor, MotorPair, Motor, PrimeHub
from spike.control import Timer
from math import *

hub = PrimeHub()
color = ColorSensor('A')
wheels = MotorPair('F', 'B')
updown = Motor('E')
sideside = Motor('C')
timer = Timer()

def followLine(wheels, color, power):
    if color.get_color() == 'black':
        wheels.start_tank( trunc(power * 0 / 3), power)
    else:
        wheels.start_tank(power, trunc(power * 0 / 3))
    
while True:
    followLine(wheels, color, 40)