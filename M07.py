# LEGO type:standard slot:1 autostart
# left black corner on first bold line touching home area, right black corner touching very beggining of fifth square on edge of table 
from spike import ColorSensor, MotorPair, Motor, PrimeHub
from spike.control import Timer, wait_for_seconds
import math

hub = PrimeHub()
color = ColorSensor('A')
wheels = MotorPair('F', 'B')
updown = Motor('C')
sideside = Motor('E')
timer = Timer(
wheels.set_motor_rotation(8.8 * math.pi, 'cm')

# Move to ship deck
wheels.move(42.87, 'in', steering=0, speed=75)

# turn right
wheels.move_tank(65,unit='degrees', left_speed=75, right_speed=None)