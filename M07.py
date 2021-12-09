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

# start


# move foward 
wheels.move(18.5, 'in', steering=55, speed=55)




# move back

