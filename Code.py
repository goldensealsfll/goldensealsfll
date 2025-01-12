from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E,Direction.CLOCKWISE)
arm_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE, [12, 36])
drive_base = DriveBase (left_wheel, right_wheel, 88, 112)

drive_base.use_gyro(True)

default_speed = 600

while True:
    selected = hub_menu("A", "B", "C", "D", "X", "E") 
    drive_base.settings(straight_speed=default_speed, turn_rate=100)
    
    if selected == "A":
        #Getting in position by turning and going straight      
        drive_base.straight(230)
        drive_base.turn(90)
        #getting away from home base 1
        drive_base.straight(265)
        #turning twards mission
        drive_base.turn(-90)
        #getting to mission and turning twards it
        drive_base.straight(410)
        drive_base.turn(-90)
        #raming into mission to complete it
        drive_base.straight(180)
        #driving away from the mission
        drive_base.straight(-150)
        #turning twards next mission
        drive_base.turn(45)
        #going to next missiion
        drive_base.straight(160)
        #puting down arm to complete mission and puting arm up
        arm_motor.run_time(-800, 1075)
        drive_base.straight(-30)
        wait(500)
        arm_motor.run_angle(1000, 180)
        #moving back to go to the next mission
        drive_base.straight(-55)
        #turnning 160 degress to turn pother way
        drive_base.turn(130)
        #driving twards next mission
        drive_base.straight(900)
        #turn twards lever
        drive_base.turn(110)
        #drive forward 
        drive_base.straight(230)
        #arm motor down
        #tuen
        drive_base.turn(100)
        #arm motor down
        arm_motor.run_angle(600, -175)
        drive_base.straight(190)
        arm_motor.run_angle(600,172)
        drive_base.straight(-225)
        
        #turn to leave the shipwreck area
        drive_base.turn(-80)
        #drive twards to crab cages
        drive_base.straight(500)
        #turn to face home base
        drive_base.turn(59)
        #Drive to home base
        drive_base.straight(1000)
        
    elif selected == "B":
        #drive forward
        drive_base.straight(230) 
        #turn twards mission
        drive_base.turn(90)
        arm_motor.run_angle(600, -180)
        #drive all the way to the mission
        drive_base.straight(250)
        #turn in front of the mission
        drive_base.turn(-90)
        #complete mission
        drive_base.straight(230)
        drive_base.turn(90)
        drive_base.straight(100)
        #arm motor up
        #arm_motor.run_time(600, 600)
        arm_motor.run_angle(200, 60)
        wait(500)
        drive_base.straight(100)
        arm_motor.run_angle(200, 20)
        drive_base.straight(40)
        wait(500)
        drive_base.straight(-200)
        arm_motor.run_angle(600, -65)
        #go closer to trident and complete it
        drive_base.turn(90)
        arm_motor.run_angle(600,80)
        drive_base.straight(320)
        drive_base.turn(-90)
        drive_base.straight(345)
        drive_base.turn(-55)
        drive_base.straight(180)
        arm_motor.run_angle(600,-70)
        drive_base.straight(-150)
        arm_motor.run_angle(600, 30)
        drive_base.straight(80)
        drive_base.turn(55)
        drive_base.straight(1000)
        drive_base.turn(90)
        drive_base.straight(500)
        


    elif selected == "C":
       # move towards green mission
       drive_base.straight(205)
       drive_base.turn(-45)
       drive_base.straight(305)
       drive_base.straight(-510)
       #start getting into position for green mission 
       #drive_base.straight(40)
       #start doing green mission
       #arm_motor.run_angle(600,-165)
       #drive_base.straight(-15)
       #drive_base.turn(-100)
       #drive_base.straight(30)
       #drive_base.turn(50)
       #drive_base.turn(-15)
       #drive_base.straight(100)
       #drive_base.turn(100)
       #go to last mission
       #drive_base.straight(70)
       #do last mission
       
    elif selected == "D":
        drive_base.straight(350)
        drive_base.turn(-45)
        drive_base.straight(370)
        drive_base.turn(90)
        drive_base.straight(240)
        drive_base.straight(-240)
        drive_base.turn(-90)
        drive_base.straight(-370)
        drive_base.turn(45)
        drive_base.straight(-300)
        wait(4600)
        drive_base.straight(150)
        drive_base.turn(45)
        drive_base.straight(500)
        drive_base.turn(-90)
        drive_base.straight(380)
        drive_base.turn(45)
        arm_motor.run_angle(600,-160)
        drive_base.straight(155)
        arm_motor.run_angle(600,20, wait=False)
        wait(2000)
        arm_motor.run_angle(600,30, wait=False)
        wait(2000)
        arm_motor.run_angle(600,5, wait=False)
        wait(2000)
        arm_motor.run_angle(600,-60)
        drive_base.straight(-160)

    elif selected == "X":
        break

    elif selected == "E":
        drive_base.straight(230)
        drive_base.turn(90)
        drive_base.straight(250)
        drive_base.turn(-90)
        drive_base.straight(500)
        arm_motor.run_angle(200, -140)
        #arm_motor.run_target(600, -200)
        drive_base.turn(90)
        drive_base.straight(200)
        drive_base.turn(-90)
        drive_base.straight(65)
        arm_motor.run_time(-200, 500)
        arm_motor.run_angle(600,30)
        drive_base.turn(35)
        drive_base.straight(-800)