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

drive_base.settings(straight_speed=500, turn_rate=100) 

while True:
    selected = hub_menu("D", "U", "S", "X") 

    if selected == "D":
       #dragon thing
       arm_motor.run_angle(300, -165)
       wait(500)
       drive_base.straight(150)
       drive_base.turn(90)
       drive_base.straight(190)
       drive_base.turn(-90)
       drive_base.straight(370)
       drive_base.turn(-90)
       arm_motor.run(-60)
       wait(1000)
       arm_motor.run(45)
       drive_base.straight(-50)


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