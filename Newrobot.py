from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E,Direction.CLOCKWISE)
right_arm_motor = Motor(Port.F, Direction.COUNTERCLOCKWISE, [12, 36])
left_arm_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [12, 36])
drive_base = DriveBase (left_wheel, right_wheel, 88, 112)

drive_base.use_gyro(True)

default_speed = 300

while True:
    selected = hub_menu("A", "B", "C", "D", "E", "F", "X", "Y", "Z") 
    drive_base.settings(straight_speed=default_speed, turn_rate=100)

    if selected == "A":
        drive_base.straight(190)
        drive_base.turn(12)
        drive_base.straight(510)
        drive_base.turn(-100)
        left_arm_motor.run_angle(100, 50)
        drive_base.straight(200)
        wait(500)
        right_arm_motor.run_time(-500, 500)
        wait(500)
        right_arm_motor.run_angle(500, 70)
        wait(1000)
        left_arm_motor.run_time(-2000, 1000)
    elif selected == "B":
        left_arm_motor.run_angle(100, 50)
        drive_base.straight(-200)
        left_arm_motor.run_angle(100, -50)
        drive_base.turn(55)
        drive_base.straight(125)
        left_arm_motor.run_angle(200, 60)
        left_arm_motor.run_angle(200, -60)
        drive_base.turn(-120)
        drive_base.straight(800)
    elif selected == "C":
        drive_base.straight(150)
        drive_base.turn(30)
        drive_base.straight(500)
        drive_base.turn(-30)
        right_arm_motor.run_angle(100,-70)
        drive_base.straight(280)
        right_arm_motor.run_angle(100,-25)
        drive_base.straight(15)
        right_arm_motor.run_angle(100,-5)
        right_arm_motor.run_angle(100,30)
        drive_base.straight(-150)
        drive_base.turn(80)
        drive_base.straight(250)
        drive_base.turn(-90)

    elif selected == "D":
        #trident mission-Natalie
        drive_base.straight(500)
        drive_base.turn(-45)
        drive_base.straight(200)
        drive_base.turn(-5)
        right_arm_motor.run_angle(500, 10000)
    elif selected == "E":
        #right side krill collection
        drive_base.straight(200)
        drive_base.turn(-20)
        drive_base.straight(150)
        drive_base.turn(35)
        drive_base.straight(150)
    elif selected == "X":
        #trident arm testing
        right_arm_motor.run_angle(100, -50)
        wait(100)
        right_arm_motor.run_angle(100, -10)

    # Nochola's changes
    elif selected == "Y":
        left_arm_motor.run_angle(500, 100, wait=False)
        drive_base.straight(420)
        left_arm_motor.run_angle(500, -80)
        drive_base.straight(-500)
    elif selected == "Z":
        left_arm_motor.run_angle(500, 120)
        drive_base.straight(540)
        left_arm_motor.run_angle(500, -100)       
        drive_base.straight(-150)
        drive_base.turn(35)
        drive_base.straight(400)
        drive_base.turn(-120)
        drive_base.straight(140)
        right_arm_motor.run_time(-100, 800, wait=True)
        wait(500)
        right_arm_motor.run_angle(75, 80)
        drive_base.straight(-120)
        left_arm_motor.run_angle(500, 100)       
        drive_base.turn(52)
        drive_base.straight(225)
        drive_base.turn(-5)
        left_arm_motor.run_angle(500, -150)       
        exit

        