# LEGO type:standard slot:0 autostart
# left wall 4 1/2 squares from wood
from spike import ColorSensor, MotorPair, Motor, PrimeHub
from spike.control import Timer, wait_for_seconds
import math

hub = PrimeHub()
color = ColorSensor('A')
wheels = MotorPair('F', 'B')
updown = Motor('C')
sideside = Motor('E')
timer = Timer()
wheels.set_motor_rotation(8.8 * math.pi, 'cm')

# move foward
wheels.move(25.5, 'in', steering=0, speed=30)

# use top attatchment to bring down the cargo in the plane
updown.run_for_rotations(0.70)

# move back
wheels.move(-1.9, 'in', steering=0, speed=50)

# move wall up
updown.run_for_rotations(-0.75)

# move top attachment to the side
sideside.run_for_rotations(-0.50)

# move forward
wheels.move(1.1, 'in', steering=0, speed=50)

# move wall down
updown.run_for_rotations(0.65, speed= 100)

# move forward
wheels.move(1.5, 'in', steering=0, speed=50)

# return to home and take toolbox with
wheels.move(-25, 'in', steering=0, speed=50)

