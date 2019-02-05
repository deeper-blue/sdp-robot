# Runs the motors gradually first for 25 cm forward and back, then for 5 cm.
# Used to test gradual movement scheme and how it adapts to long and short distances.
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
    movement = move.Gradual(circ)

    # Move forward by 58 cm and back
    movement.move(twins, -58)
    movement.move(twins,  58)

    # Move forward by 5 cm and back
    movement.move(twins, -5)
    movement.move(twins,  5)

iteration()
