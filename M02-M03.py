# LEGO type:standard slot:0 autostart
# left wall 4 1/2 squares from wood
from spike import ColorSensor, MotorPair, Motor, PrimeHub
from spike.control import Timer
import math

hub = PrimeHub()
color = ColorSensor('A')
wheels = MotorPair('F', 'B')
updown = Motor('C')
sideside = Motor('E')
timer = Timer()

# move foward
wheels.move(11 * math.pi / 2, 'in', steering=0, speed=30)

# use top attatchment to bring down the cargo in the plane
updown.run_for_rotations(0.75)

# move back 
wheels.move(-1 * math.pi / 2, 'in', steering=0, speed=50)

# move wall up
updown.run_for_rotations(-0.75)

# move forward
wheels.move(0.5 * math.pi / 2, 'in', steering=0, speed=50)

# move wall down
updown.run_for_rotations(0.65, speed= 100)
