# Runs the motors uniformly first for 25 cm forward and back, then for 5 cm.
# Used to test uniform movement scheme and how it adapts to long and short distances.
#
# Authors:
#   Filip Smola

import ev3dev.ev3 as ev3
import time
import math
import motor
import move

# Wheel circumference
circ = 12.9 # in cm

def iteration():
    print("iteration entry")

    # Get twin motors
    twins = motor.Twin(motor.portA, motor.portB)

    # Prepare movement
    movement = move.Uniform(circ)

    # Move forward by 50 cm and back
    movement.move(twins, -50)
    movement.move(twins,  50)

    # Move forward by 10 cm and back
    movement.move(twins, -10)
    movement.move(twins,  10)

ev3.Sound.speak('Do not interfere with the robot. Testing in progress.').wait()
iteration()
