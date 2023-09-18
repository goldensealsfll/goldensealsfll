
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor,ColorDistanceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch, hub_menu
from pybricks.parameters import Icon

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)
arm_motor = Motor(Port.C)
drive_base = GyroDriveBase(left_wheel, right_wheel, 88, 112)

drive_base.settings(straight_speed=100, turn_rate=100)

while True:
    selected = hub_menu("B","Y","G")

    if selected == "B":
        #move forward
        drive_base.straight(700)
        drive_base.turn(45)
        drive_base.straight(135)
        drive_base.straight(-135)
        drive_base.turn(45) 
        drive_base.straight(270) 
        drive_base.turn(-60) 
        drive_base.straight(-270)
    elif selected == "Y":
        break

