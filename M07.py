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

# move foward
wheels.move(9, 'in', steering=0, speed=30)

# turn to hit car 
wheels.move(178, 'degrees', steering=100, speed=20)

# move foward to hit car
wheels.move(13.8, 'in', steering=0, speed=40)

# move back 
wheels.move(-2, 'in', steering=0, speed=20)

# turn to face the thing
wheels.move(-137,'degrees', steering=79, speed=25)

# go to the thing
wheels.move(14, 'in', steering=0, speed=25)

# turn to the thing
wheels.move(130, 'degrees', steering=80, speed=25)

# move foward
wheels.move(6.7, 'in', steering=0, speed=30)

#move back
wheels.move(-7, 'in', steering=0, speed=35)

# turn
wheels.move(185, 'degrees', steering=53, speed=35)

# Move forward
wheels.move(11, 'in', steering=0, speed=35)

# Turn left to helicopter
wheels.move(155, 'degrees', steering=-115, speed=35)

#Move forward
wheels.move(15, 'in', steering=0, speed=35)

# move back
wheels.move(-6, 'in', steering=0, speed=20)

# turn
wheels.move(250, 'degrees', steering=205, speed=20)

# move foward
wheels.move(3, 'in', steering=0, speed=20)

# turn again
wheels.move(210, 'degrees', steering=156, speed=20)

# move foward
wheels.move(13, 'in', steering=0, speed=30)

# move wall up
updown.run_for_rotations(-100, speed=80)

# move foward
wheels.move(17, 'in', steering=0, speed=30)

# turn
wheels.move(-140, 'degrees', steering=75, speed=20)

# move foward 
wheels.move(35, 'in', steering=0, speed=30)

