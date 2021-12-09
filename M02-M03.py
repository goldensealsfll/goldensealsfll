# LEGO type:standard slot:0 autostart
# left wall 4 1/2 squares from wood
from spike import ColorSensor, MotorPair, Motor, PrimeHub
from spike.control import Timer, wait_for_seconds
import math

hub = PrimeHub()
wheels = MotorPair('F', 'B')
updown = Motor('C')
sideside = Motor('E')
timer = Timer()
wheels.set_motor_rotation(8.8 * math.pi, 'cm')

# move foward
wheels.move(25.7, 'in', steering=0, speed=30)

# use top attatchment to bring down the cargo in the plane
updown.run_for_rotations(0.75)

# move back
wheels.move(-1.9, 'in', steering=0, speed=50)

# move wall up
updown.run_for_rotations(-0.90)

# move forward
wheels.move(1.3, 'in', steering=0, speed=50)

# move wall down
updown.run_for_rotations(0.75, speed= 100)

# move forward
count = 0
while (count < 3):
    count = count + 1
    wheels.move(2, 'in', steering=0, speed=75)
    wheels.move(-2, 'in', steering=0, speed=75)

# return to home and take toolbox with
wheels.move(-24, 'in', steering=0, speed=50)
