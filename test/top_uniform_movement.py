# Run the motor for 50 cm, first one way and then back. Then run for 10 cm, forward and back.
# Test to see how well the motor performs on the entire length of the track and on a short part of it.
# Author(s)
# Jeremy Scott
# Derenik Pogosyan

import ev3dev.ev3 as ev3
import time
import math
import motor
import move

# Wheel circumference
circ = 12.9 # in cm

def iteration():
    print("iteration entry")

    # Get motor
    motorC = motor.Single(motor.portC)

    # Prepare movement
    movement = move.Uniform(circ)
    movement.speed_long = 200
    movement.speed_short = 100

    # Move long distance
    movement.move(motorC, 50)
    movement.move(motorC, -50)

    # Move short distance
    movement.move(motorC, 10)
    movement.move(motorC, -10)

iteration()
