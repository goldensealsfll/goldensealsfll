# LEGO type:standard slot:1 autostart
# left black corner on first bold line touching home area, right black corner touching very beggining of fifth square on edge of table 
from spike import ColorSensor, MotorPair, Motor, PrimeHub
from spike.control import Timer, wait_for_seconds
import math

hub = PrimeHub()
wheels = MotorPair('F', 'B')
wheel1= Motor('B')
updown = Motor('C')
sideside = Motor('E')
timer = Timer
wheels.set_motor_rotation(8.8 * math.pi, 'cm')

# move foward
wheels.move(13, 'in', steering=0, speed=30)

# turn to hit car 
wheels.move(184, 'degrees', steering=107, speed=20)

# move foward to hit car
wheels.move(24, 'in', steering=0, speed=40)

# move back 
wheels.move(-4.5, 'in', steering=0, speed=20)

# turn to face the thing
wheels.move(-137,'degrees', steering=79, speed=25)

# go to the thing
wheels.move(18.5, 'in', steering=0, speed=30)

# turn to the thing
wheels.move(130, 'degrees', steering=75, speed=30)

# move foward
wheels.move(8, 'in', steering=0, speed=30)

#move back
wheels.move(-10, 'in', steering=0, speed=35)

# turn
wheels.move(195, 'degrees', steering=50, speed=35)

# Move forward
wheels.move(10, 'in', steering=0, speed=35)

# Turn left
wheels.move(150, 'degrees', steering=-90, speed=35)

#Move forward
wheels.move(25, 'in', steering=0, speed=35)

# move back
wheels.move(-7, 'in', steering=0, speed=20)

# turn
wheels.move(230, 'degrees', steering=180, speed=20)

# move foward
wheels.move(6, 'in', steering=0, speed=20)

# turn again
wheels.move(200, 'degrees', steering=150, speed=20)

# move foward
wheels.move(15, 'in', steering=0, speed=30)

# move wall up
updown.run_for_rotations(-100, speed=80)

# move foward
wheels.move(19, 'in', steering=0, speed=30)

# turn
wheels.move(-140, 'degrees', steering=75, speed=20)

# move foward 
wheels.move(35, 'in', steering=0, speed=30)