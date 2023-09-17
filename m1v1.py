from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch, hub_menu


hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E)
arm_motor = Motor(Port.C)
drive_base = GyroDriveBase(left_wheel, right_wheel, 88, 112)

drive_base.settings(straight_speed=100, turn_rate=100)

print("Entering menu\n")

while True:
    selected = hub_menu("T", "L", "C", "X")

    if selected == "L":
        #3D Cinema
        ##Go forward:
        drive_base.straight(350)
        ##lower arm:
        arm_motor.run_angle(360*2, 330)
        ##lift arm
        ##turn 90
        ##forward
    if selected == "X":
        break