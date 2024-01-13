from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Axis, Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
left_wheel = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_wheel = Motor(Port.E,Direction.CLOCKWISE)
arm_motor = Motor(Port.C)
drive_base = DriveBase (left_wheel, right_wheel, 88, 112)

drive_base.use_gyro(True)

default_speed = 300
drive_base.settings(straight_speed=default_speed, turn_rate=100)

while True:
    selected = hub_menu("A", "B", "C", "D", "X") 

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
        arm_motor.run_until_stalled(-100, then=Stop.COAST)

        
        #Turning and moving backwards to get onto position to move to the stage
        drive_base.settings(straight_speed=200, turn_rate=100)
        drive_base.turn(-10)
        drive_base.straight(-200)
        drive_base.settings(straight_speed=default_speed)

        #Turning and moving to statue (moving hand up)
        drive_base.turn(28)
        arm_motor.run_angle(200,200,wait=False)
        drive_base.straight(400)
        
        #Turning to statue and getting in position for statue
        drive_base.turn(-50)
        drive_base.straight(450)
        drive_base.turn(120)
        drive_base.straight(35)
        arm_motor.run_time(-300, 1500, then=Stop.COAST)
        drive_base.turn(75)
        drive_base.straight(750)
        drive_base.turn(65)
        drive_base.straight(400)

    elif selected == "B":
        drive_base.straight(2500)

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
        drive_base.straight(35)

        #arm motor goes down to move the bannana boat
        arm_motor.run_angle(150, -215, wait=False)
        wait(3000)

        #handle the case where the arm gets stuck on the block
        if arm_motor.stalled():
            hub.speaker.beep()
            arm_motor.run_angle(150, 20)
            drive_base.straight(-20)
            arm_motor.run_angle(150, -20)

        #start moving backwards to the target area
        drive_base.settings(straight_speed=200, turn_rate=100)
        drive_base.straight(-125)
        drive_base.settings(straight_speed=default_speed)

        # arm motor goes up to be ready for next mission
        arm_motor.run_angle(150, 210)

        #pseudocode for rolling camera

        #go back to make sure that robot doesn't ram into banana boat camera
        drive_base.straight(-95)

        #turn left to go to the orange thing
        drive_base.turn(-65)

        #go straight to go to the orange thing
        drive_base.straight(375)

        #turn to face the orange thing
        drive_base.turn(120)

        #move straight to ram the whight thing in front of orange arm(thing)
        drive_base.straight(350)

        #move arm motor down to hit orange thing to free the rollercoaster
        arm_motor.run_angle(230, -200)

        #move back up to get the attachment out with out knoking the orange thing on 
        drive_base.straight(-25)

        #move arm motor up
        arm_motor.run_angle(100, 20)

        #move backwards
        drive_base.straight(-90)

        #turn to movie set
        drive_base.turn(-90)

        #move arm motor sown
        arm_motor.run_angle(150, -15)

        #move straight to movir set
        drive_base.straight(510)

        #turn to movie set
        drive_base.turn(90)

        #move twards the camera
        drive_base.straight(105)

        #arm motor down for the camera
        arm_motor.run_angle(100, -15)

        #turn to move the camera

        drive_base.turn(65)

        #arm motor goes up
        arm_motor.run_angle(400, 220)

        #move backwards to the next mission
        drive_base.straight(-50)

        #turn to go to timersive experience
        drive_base.turn(25)

        #movestraight to go through the colorful thingamo=abop
        drive_base.straight(200)

        #turn to timersive experience
        drive_base.turn(90)

        #drive twards timersve experience
        drive_base.straight(640)

        #turn to go to timersive experience
        drive_base.turn(-90)

        #move forward to be at timersive experience
        drive_base.straight(590)

        #turn to face the timersive experience
        drive_base.turn(90)

        #move forward
        drive_base.straight(170)

        #turn to timersive experience
        drive_base.turn(95)

        #arm motor down
        arm_motor.run_angle(300, -220)
        wait(1000)

        #TODO: stall detection needs to be improved
        if arm_motor.stalled():
            hub.speaker.beep()
            wait(1000)

        #move forward
        drive_base.straight(20)

        #move up the arm motor
        arm_motor.run_angle(400, 60)

        #turn to go back home
        drive_base.turn(-25)

        #move backward
        drive_base.straight(-170)

        #turn to go to home
        drive_base.turn(110)

        #go straight 
        drive_base.straight(200)

        #turn
        drive_base.turn(45)

        #move forward
        drive_base.straight(800)

    elif selected == "D":
        drive_base.straight(200)
        drive_base.turn(90)
        drive_base.straight(265)
        drive_base.turn(-47)
        arm_motor.run_angle(700, -220)
        drive_base.straight(125)
        arm_motor.reset_angle(0)
        arm_motor.dc(100)
        wait(1000)
        while arm_motor.angle() < 100:
            drive_base.straight(-20)
            drive_base.straight(20)



    
    elif selected == "X":
        drive_base.straight(300)
        wait(1000)
        drive_base.straight(-400)
