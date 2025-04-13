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

default_speed = 350

while True:
    selected = hub_menu("1", "2", "3", "4", "5", "6") 
    drive_base.settings(straight_speed=default_speed, turn_rate=100)

    if selected == "4":
        right_arm_motor.run_angle(100, -65)
        drive_base.straight(330)
        drive_base.turn(35)
        drive_base.straight(520)
        drive_base.turn(-30)
        drive_base.straight(60)
        right_arm_motor.run_angle(100, 90)
        right_arm_motor.run_angle(100, -30, wait=True)
        drive_base.straight(-80)
        drive_base.turn(40)
        drive_base.straight(-220)
        drive_base.turn(45)
        drive_base.straight(-50)
        right_arm_motor.run_angle(100, 35)
        drive_base.straight(80)
        right_arm_motor.run_angle(100, -120, wait=True)
        drive_base.straight(140)
        drive_base.straight(-250)
        right_arm_motor.run_angle(100, -30, wait=False)
        drive_base.turn(40)
        drive_base.straight(500)
        drive_base.turn(-80)
        drive_base.straight(170)
        drive_base.turn(-15)
        ##
        right_arm_motor.run_angle(100, 80)
        drive_base.settings(straight_speed=1000, turn_rate=100)
        drive_base.straight(-160)
        drive_base.settings(straight_speed=default_speed, turn_rate=100)
        drive_base.turn(50)
        drive_base.straight(800)
        drive_base.turn(45)
        drive_base.straight(400)
    
    elif selected == "1":
       #colection mission
       right_arm_motor.run_angle(800, -280, wait=False)
       drive_base.straight(400)
       right_arm_motor.run_angle(800, 170, wait=False)
       drive_base.straight(260)
       right_arm_motor.run_angle(800, -100, wait=False) 
       drive_base.settings(straight_speed=200, turn_rate=60)     
       drive_base.turn(-75)
       drive_base.settings(straight_speed=default_speed, turn_rate=100)
       drive_base.straight(300)
       drive_base.turn(-15)
       right_arm_motor.run_angle(800, -85, wait=False)
       drive_base.straight(330)
       drive_base.turn(30)
       drive_base.straight(250)
       drive_base.turn(-45)
       drive_base.straight(400)
       drive_base.turn(-55)
       drive_base.straight(700)
       break
    elif selected == "5":
       #run 5
       drive_base.straight(420)
       drive_base.turn(-48)
       drive_base.straight(195)
       drive_base.straight(-50)
       drive_base.turn(30)
       drive_base.straight(85)
       drive_base.turn(56)
       right_arm_motor.run_angle(200, -130, wait=False)
       drive_base.straight(385)
       left_arm_motor.run_angle(100, -50, wait=True)
       drive_base.straight(-60)
       drive_base.turn(30)
       drive_base.straight(20)
       right_arm_motor.run_angle(500, 130)
       drive_base.straight(-180)
       drive_base.turn(-70)
       drive_base.straight(-800)

    elif selected == "6":
       #sonar discovery, submercible, octopus in ring
       drive_base.turn(-5.5)
       drive_base.straight(500) 
       left_arm_motor.run_angle(100, 50, wait=False)     
       drive_base.straight(410)
       left_arm_motor.run_time(-50, 3000)
       left_arm_motor.run_angle(100, -25, wait=False)     
       drive_base.straight(-200)
       drive_base.turn(-70)
       right_arm_motor.run_angle(100, -70, wait=False)
       drive_base.straight(535)
       right_arm_motor.run_time(100, 1000, wait=True)
       drive_base.straight(-50)
       drive_base.turn(55)
       drive_base.straight(-100)
    elif selected == "2":
        #coral tree pick up
        drive_base.turn(-1)
        left_arm_motor.run_angle(500, 100, wait=False)
        drive_base.straight(420)
        left_arm_motor.run_angle(500, -80)
        drive_base.straight(-500)
    elif selected == "3":
        #hanging coral tree, coral buds, picking up scuba diver, and shark
        left_arm_motor.run_angle(500, 120)
        drive_base.straight(540)
        left_arm_motor.run_angle(500, -100)       
        drive_base.straight(-150)
        drive_base.turn(35)
        drive_base.straight(375)
        drive_base.turn(-120)
        drive_base.straight(120)
        right_arm_motor.run_time(-50, 1000, wait=True)
        wait(500)
        right_arm_motor.run_angle(75, 80)
        drive_base.straight(-120)
        left_arm_motor.run_angle(500, 100)       
        drive_base.turn(52)
        drive_base.straight(225)
        drive_base.turn(-5)
        left_arm_motor.run_angle(500, -150)
        left_arm_motor.run_angle(500, 150)
        drive_base.straight(-200)
        drive_base.turn(50)
        drive_base.straight(-800)
        break
        