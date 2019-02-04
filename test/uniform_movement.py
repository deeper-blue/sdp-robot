# Runs the motors uniformly first for 25 cm forward and back, then for 5 cm.
# Used to test uniform movement scheme and how it adapts to long and short distances.
#
# Authors:
#   Filip Smola

import ev3dev.ev3 as ev3
import time
import math
import motor

# Maximum and minimum speed (in %)
max_v_long = 300
max_v_short = 100

# Wheel circumference
circ = 12.9 # in cm

# Distance considered long (in degrees)
long_distance = 15 / circ * 360

# Move the motor uniformly by relative distance (in cm)
def move_uniform(motor, rel_dist):
    print("move_uniform entry")

    # Compute target rotational distance (in degrees)
    rel_pos = rel_dist / circ * 360

    # Pick speed
    max_v = max_v_long if (math.fabs(rel_pos) >= long_distance) else max_v_short

    # Run motor for computed distance at max speed
    motor.run_to_rel_pos(rel_pos, max_v)
    motor.wait_while('running')

def iteration():
    print("iteration entry")

    # Get twin motors
    twins = motor.Twin(motor.portA, motor.portB)

    # Move forward by 50 cm and back
    move_uniform(twins, -50)
    move_uniform(twins, 50)

    # Move forward by 10 cm and back
    move_uniform(twins, -10)
    move_uniform(twins, 10)

ev3.Sound.speak('Do not interfere with the robot. Testing in progress.').wait()
iteration()
