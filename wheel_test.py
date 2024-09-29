from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E,Direction.CLOCKWISE)
arm_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
drive_base = DriveBase (left_wheel, right_wheel, 81.6, 140)

drive_base.use_gyro(True)

default_speed = 1000
while True:
    selected = hub_menu("A", "B", "C", "D", "X") 
    drive_base.settings(straight_speed=default_speed, turn_rate=300)

    if selected == "A":

        # Main Test:
    # Straight really fast
    # Abrupt stop
    # Turn right using both wheels, then turn left with both wheels
    # Abrupt stop
    # Backward really fast
    # Abrupt stop
    # Turn right using left wheel
    # Turn left using right wheel
        wait(1000)
        drive_base.straight(1500)
        drive_base.turn(450)
        drive_base.turn(-450)
        drive_base.straight(-1500)