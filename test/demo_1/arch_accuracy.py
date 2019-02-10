# Faclitates testing of arch movement accuracy.
# Moves the arch 50 cm and stops there.
#
# Authors:
#   Filip Smola

import ev3dev.ev3 as ev3
import math
import motor
import move

# Wheel radius
radius = 2.1

def iteration():
    print("iteration entry")

    # Get twin motors
    twins = motor.Twin(motor.portA, motor.portB)

    # Prepare movement and move 50 cm
    movement = move.Gradual(2 * math.pi * radius)
    movement.move(twins, -50)

iteration()
