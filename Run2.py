
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

drive_base.settings(straight_speed=300, turn_rate=100)

while True:
    selected = hub_menu("B","G","Y")

    if selected == "B":
        #Getting in position by turning and going straight  to move forward to concert stage
        #drive_base.straight(160)
        #drive_base.turn(-90)
        #drive_base.straight(230)
        #drive_base.turn(90)

        #move forward to music concert, turning, and pushing in concert stage
        #drive_base.straight(540)
        #drive_base.turn(45)
        #drive_base.straight(135)

        #Moving back from pushing in mission
        #drive_base.straight(-135)
        
        #Turning to go forward
        #drive_base.turn(45)
        
        #Going forward to pull back lever, turning, and pulling back lever of lights
        #drive_base.straight(225)
        #drive_base.turn(-45)
        #arm_motor.run_angle(600,-125)
        
        #Turning to move backwards and away from music concert
        #drive_base.turn(-30)
        #drive_base.straight(-450)

        #Turning, going forward to push in craft creator
        #drive_base.turn(-60)
        #drive_base.straight(350)
        
        #Using arm to lift back craft creator lid
        #arm_motor.run_angle(100,-85)
        #wait(10)
        #arm_motor.run_angle(100, 15)
        
        #Turning and moving backwards to get onto position to move to the stage
        #drive_base.turn(-10)
        #drive_base.straight(-200)

        #Turning and moving to statue
        drive_base.turn(20)
        drive_base.straight(400)
        
        #Turning to statue and getting in position for statue
        drive_base.turn(-30)
        drive_base.straight(400)
        drive_base.turn(120)
        drive_base.straight(50)
        arm_motor.run_angle(200,-200)
        drive_base.turn(80)
        drive_base.straight(150)





    
    if selected == "G":
        drive_base.straight(700)
    elif selected == "Y":
        break

