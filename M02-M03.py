# LEGO type:standard slot:0 autostart

from spike import ColorSensor, MotorPair, Motor, PrimeHub
from spike.control import Timer
from math import *

hub = PrimeHub()
color = ColorSensor('A')
wheels = MotorPair('F', 'B')
updown = Motor('E')
sideside = Motor('C')
timer = Timer()

# move foward
# use the bottom attatchment to move the cargo package into the home base
# move foward
# use top attatchment to bring down the cargo in the plane
# turn & go straight int the home base