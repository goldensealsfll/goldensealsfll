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
    selected = hub_menu("A", "B", "C", "D", "X")
    
    if selected == "A":
        #Getting in position by turning and going straight      
        drive_base.straight(230)
        drive_base.turn(90)
        #getting away from home base 1
        drive_base.straight(150)
        #turning twards mission
        drive_base.turn(-90)
        #getting to mission and turning twards it
        drive_base.straight(250)
        drive_base.turn(90)
        #raming into mission to complete it
        drive_base.straight(100)
        #driving away from the mission
        drive_base.straight(-100)
        #turning twards next mission
        drive_base.turn(-45)
        #going to next missiion
        drive_base.straight(150)
        #puting down arm to complete mission
        arm_motor.run_angle(600, -100)
        #moving back to go to the next mission
        drive_base.straight(-150)
        #turnning 160 degress to turn pother way
        drive_base.turn(160)
        #driving twards next mission
        drive_base.straight(300)
        #turn twards lever
        drive_base.turn(120)
        #drive forward and backwards to push lever
        drive_base.straight(100)
        drive_base.straight(-200)
        #turn to to to the trident
        drive_base.turn(45)
        #drive twards to crab cages
        drive_base.straight(300)
        #turn to get closer to trident
        drive_base.turn(90)
        #drive forward to get in front of trident
        drive_base.straight(200)
        #turn to the trident
        drive_base.turn(120)
        #lift up arm motor
        arm_motor(600, 30)
        #drive into trident to complete it
        drive_base.straight(150)
        #move backwards
        drive_base.straight(-200)
        #turn to home base
        drive_base.turn(100)
        #go back to home
        drive_base.straight(500)
        
    elif selected == "B":
        #drive forward
        drive_base.straight(100) 
        #turn twards mission
        drive_base.turn(90)
        #drive all the way to the mission
        drive_base.straight(500)
        #turn in front of the mission
        drive_base.turn(-135)
        #complete mission
        drive_base.straight(150)
        #drive away from the mission to the next
        drive_base.straight(-150)
        #turn twards next mission
        drive_base.turn(45)
        #drive twards next mission
        drive_base.straight(300)
        #turn into the mission
        drive_base.turn(135)
        #arm motor down
        arm_motor(600, 30)
        #move into mission with the motor down to complete the banana boat mission
        drive_base.straight(150)
        #arm motoer up
        arm_motor(600,30)
        #move away from mission
        drive_base.straight(-150)
        #tuen twards home and go to home
        drive_base.turn(100)
        drive_base.staright(500)



    elif selected == "C":
       # move towards green mission
       drive_base.straight(600)
       drive_base.turn(-90)
       #start getting into position for green mission 
       drive_base.straight(30)
       drive_base.turn(90)
       drive_base.straight(30)
       #start doing green mission
       arm_motor(600,-100)
       drive_base.turn(175)
       drive_base.straight(100)
       drive_base.turn(50)
       drive_base.turn(-15)
       drive_base.straight(100)
       drive_base.turn(100)
       #go to last mission
       drive_base.straight(70)
       drive_base.turn(-90)
       #do last mission
       arm_motor(600,100)



    elif selected == "X":
        break