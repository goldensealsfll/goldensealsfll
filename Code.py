from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks. parameters import Axis, Button, Color, Direction, Port, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, hub_menu

hub = Primehub(top_side=Axis.Z, front_side=-Axis.Y)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = (Port.E)
arm_motor = Motor(Port.C)
drive_base = GyroDriveBase(left_wheel, right_wheel, 88, 112)

drive_base.settings(strait_speed=100, turn_rate=100)

while True:
    selected = hub_menu("1", "2", "3", "4", "5")
    
    if selected == "1":
        drive_base.straight(100)
    
    elif selected == "5":
        break
        