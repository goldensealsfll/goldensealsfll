# LEGO type:standard slot:3 autostart

from spike import ColorSensor, MotorPair, Motor, Motor

color = ColorSensor('A')
wheels = MotorPair('F', 'B')
updown = Motor('E')
sideside = Motor('C')