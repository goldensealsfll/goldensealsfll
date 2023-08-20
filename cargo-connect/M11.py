# LEGO type:standard slot:3 autostart
from spike import PrimeHub, Motor, MotorPair, App, LightMatrix
from spike.control import wait_for_seconds,
# how to set up: # left black corner on first bold line touching home area, right black corner touching very beggining of fifth square on edge of table 

hub = PrimeHub()
wheel1 = Motor('B')
wheels = MotorPair('F','B')
updown = Motor('C')
sideside = Motor('E')

# move wall up
updown.run_for_rotations(-30, speed=60)

# move foward
wheels.move(4.8, 'in', steering=0, speed=25)

# turn to get ready to hit bridge down
wheels.move(180, 'degrees', steering=101, speed=25)

#go foward
wheels.move(23, 'in', steering=0, speed=30)

# turn
wheels.move(75, 'degrees', steering=60, speed=25)

#go foward
wheels.move(8.5, 'in', steering=0, speed=15)

# turn to to the mail drop
wheels.move(70, 'degrees', steering=-35, speed=10)

# drop off the package
sideside.run_for_rotations(-0.45, speed=35)
wait_for_seconds(3)

# move wall up
updown.run_for_rotations(-170, speed=100)

# put the attachment up
sideside.run_for_rotations(0.45, speed=40)

# MOVE BACK
wheels.move(-7, 'in', steering=0, speed=20)

# turn 
wheels.move(140, 'degrees', steering=70, speed=20)

# move foward
wheels.move(15, 'in', steering=0, speed=30)

# turn 
wheels.move(140, 'degrees', steering=70, speed=20)

# move foward 
wheels.move(15, 'in', steering=0, speed=30)

# turn again
wheels.move(140, 'degrees', steering=70, speed=20)
