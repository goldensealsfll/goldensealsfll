from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E,Direction.CLOCKWISE)
arm_motor = Motor(Port.C)
drive_base = GyroDriveBase (left_wheel, right_wheel, 88, 112)

drive_base.settings(straight_speed=300, turn_rate=100) 

while True:
    selected = hub_menu("A", "B", "C", "X") 

    if selected == "A":
        #Getting in position by turning and going straight  to move forward to concert stage
        drive_base.straight(160)
        drive_base.turn(-90)
        drive_base.straight(230)
        drive_base.turn(90)

        #move forward to music concert, turning, and pushing in concert stage
        drive_base.straight(540)
        drive_base.turn(45)
        drive_base.straight(135)

        #Moving back from pushing in mission
        drive_base.straight(-135)
        
        #Turning to go forward
        drive_base.turn(45)
        
        #Going forward to pull back lever, turning, and pulling back lever of lights
        drive_base.straight(210)
        drive_base.turn(-45)
        arm_motor.run_angle(600,-135)
        
        #Turning to move backwards and away from music concert
        drive_base.turn(-30)
        drive_base.straight(-450)

        #Turning, going forward to push in craft creator
        drive_base.turn(-60)
        drive_base.straight(345)
        
        #Using arm to lift back craft creator lid
        arm_motor.run_angle(100,-80)
        wait(10)
        arm_motor.run_angle(100, 15)
        
        #Turning and moving backwards to get onto position to move to the stage
        drive_base.turn(-10)
        drive_base.straight(-200)

        #Turning and moving to statue (moving hand up)
        drive_base.turn(23)
        drive_base.straight(400)
        arm_motor.run_angle(200,200)

        
        #Turning to statue and getting in position for statue
        drive_base.turn(-37)
        drive_base.straight(400)
        drive_base.turn(120)
        drive_base.straight(35)
        arm_motor.run_angle(200,-215)
        drive_base.turn(75)
        drive_base.straight(175)

        #Heading back to home base
        drive_base.turn(45)
        drive_base.straight(100)
        arm_motor.run_angle(200,200)
        drive_base.turn(-70)
        drive_base.straight(900)

    elif selected == "B":
        drive_base.straight(1750)

    elif selected == "C":
        #bannana boat
        #move forward from initial start postition
        drive_base.straight(90)

        #turn to the bannana boat
        drive_base.turn(90)

        #drive towards the movie set
        drive_base.straight(600)     

        #turn so we can leave the camera in the intended area
        drive_base.turn(35)

        #drive forward a little to reach the camera
        drive_base.straight(29)

        #arm motor goes down to move the bannana boat
        arm_motor.run_angle(150, -215)

        #start moving backwards to the target area
        drive_base.straight(-125)

        wait(250)

        # arm motor goes up to be ready for next mission
        arm_motor.run_angle(150, 210)

        #pseudocode for rolling camera

        #go back to make sure that robot doesn't ram into banana boat camera
        drive_base.straight(-95)

        #turn left to go to the orange thing
        drive_base.turn(-65)

        #go straight to go to the orange thing
        drive_base.straight(350)

        #turn to face the orange thing
        drive_base.turn(120)

        #move straight to ram the whight thing in front of orange arm(thing)
        drive_base.straight(350)

        #move arm motor down to hit orange thing to free the rollercoaster
        arm_motor.run_angle(230, -200)

        #move back up to get the attachment out with out knoking the orange thing on 
        drive_base.straight(-20)

        #move arm motor up
        arm_motor.run_angle(100, 15)

        #move backwards
        drive_base.straight(-90)

        #turn to movie set
        drive_base.turn(-90)

        #move straight to movir set
        drive_base.straight(500)

        #turn to movie set
        drive_base.turn(90)

        #move twards the camera
        drive_base.straight(130)

        #arm motor down for the camera
        arm_motor.run_angle(100, -22)

        #turn to move the camera

        drive_base.turn(65)

        #arm motor goes up
        arm_motor.run_angle(400, 220)

        #move backwards to the next mission
        drive_base.straight(-50)

        #turn to go to timersive experience
        drive_base.turn(25)

        #movestraight to go through the colorful thingamo=abop
        drive_base.straight(130)

        #turn to timersive experience
        drive_base.turn(90)

        #drive twards timersve experience
        drive_base.straight(600)

        #turn to go to timersive experience
        drive_base.turn(-90)

        #move forward to be at timersive experience
        drive_base.straight(360)

        #turn to face the timersive experience
        drive_base.turn(90)

        #move forward
        drive_base.straight(20)

        #move arm motor down
        arm_motor.run_angle(400,-210)
        wait(1000)

        #move up the arm motor
        arm_motor.run_angle(400, 170)
    
    elif selected == "X":
       break   