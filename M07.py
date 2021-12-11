# LEGO type:standard slot:1 autostart
# left black corner on first bold line touching home area, right black corner touching very beggining of fifth square on edge of table 
from spike import ColorSensor, MotorPair, Motor, PrimeHub
from spike.control import Timer, wait_for_seconds
import math

hub = PrimeHub()
wheels = MotorPair('F', 'B')
updown = Motor('C')
sideside = Motor('E')
timer = Timer
wheels.set_motor_rotation(8.8 * math.pi, 'cm')

# move foward
wheels.move(13, 'in', steering=0, speed=30)

# turn to hit car 
wheels.move(178, 'degrees', steering=100, speed=20)

# move foward to hit car
wheels.move(21.5, 'in', steering=0, speed=55)

# move back 
wheels.move(-6, 'in', steering=0, speed=20)

# turn to face the thing
wheels.move(-137,'degrees', steering=79, speed=25)

# go to the thing
wheels.move(18, 'in', steering=0, speed=50)

# turn to the thing
wheels.move(140, 'degrees', steering=80, speed=30)

# move foward
wheels.move(17, 'in', steering=0, speed=50)

#move back
wheels.move(-5, 'in', steering=0, speed=35)