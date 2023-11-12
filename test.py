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
    selected = hub_menu("D", "U", "S", "X") 

    if selected == "D":
   #bannana boat
      # move forward from initial start postition
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
       arm_motor.run_angle(105, -215)

       #start moving backwards to the target area
       drive_base.straight(-125)

       wait(500)

       # arm motor goes up to be ready for next mission
       arm_motor.run_angle(100, 210)
       

       break

    elif selected == "U":
       
       #Immersive experience
       arm_motor.run_angle(300, 200)
       wait(500)
       drive_base.straight(675)
       drive_base.turn(-90)
       drive_base.straight(450)
       arm_motor.run_angle(1000, -200)
       wait(1000)
       arm_motor.run_angle(400, 200)
       drive_base.turn(-90)
       drive_base.straight(440)
       drive_base.turn(45)
       arm_motor.run_angle(600, -210)
       drive_base.straight(-40)
       arm_motor.run_angle(600, 60)
       drive_base.straight(40)
       arm_motor.run_angle(600, -80)

       break 
      
      
      

    elif selected == "X":
       break