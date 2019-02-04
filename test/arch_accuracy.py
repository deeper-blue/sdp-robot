# Faclitates testing of arch movement accuracy.
# Moves the arch 50 cm and stops there.
#
# Authors:
#   Filip Smola

import ev3dev.ev3 as ev3
import time
import math
import motor

# Position polling delay (in s)
poll_t = 0.1

# Maximum and minimum speed (in %)
max_v_long = 70
max_v_short = 40
min_v = 20

# Wheel circumference
radius = 2.1 # in cm
circ = 2 * math.pi * radius # in cm

# Distance considered long (in degrees)
long_distance = 15 / circ * 360

# Valid speeds set (multiples of 5 from min_v to max_v)
# Note: assuming this set is in increasing order
valid_speeds = [z for z in range(min_v,max_v_long + 1) if z%5 == 0]

# Linear guide function
def linear_guide(target_distance, x):
    # Select max speed
    max_v = max_v_long if (target_distance >= long_distance) else max_v_short

    # Return zero outside of supported range
    if x < 0:
        return 0
    if x > target_distance:
        return 0
    
    return - math.fabs(- (2 * max_v / target_distance) * (x - (target_distance / 2))) + max_v

# Sine guide function
def sine_guide(target_distance, x):
    # Select max speed
    max_v = max_v_long if (target_distance >= long_distance) else max_v_short

    # Return zero outside of supported range
    if x < 0:
        return 0
    if x > target_distance:
        return 0

    return max_v * math.sin(math.pi * x / target_distance)

# Move the motor gradually by relative distance (in cm)
def move_gradual(motor, rel_dist):
    print("move_gradual entry")

    # Extract direction
    direction = math.copysign(1.0, rel_dist)
    rel_dist = math.fabs(rel_dist)

    # Compute relative position in degrees
    rel_pos = rel_dist / circ * 360

    # Get current position and limit
    start = motor.get_position()

    # Main loop
    position = start
    while math.fabs(position - start) < rel_pos:
        # Compute position progress
        d = position - start

        # Remove sign
        d = math.fabs(d)

        # Compute desired speed
        desired = sine_guide(rel_pos, d)

        # Select least greater valid speed or min_v
        desired = next((x for x in valid_speeds if x > desired), min_v)

        # Reintroduce direction
        desired = direction * desired

        # Set desired speed
        motor.run_direct(desired)

        # Delay
        time.sleep(poll_t)

        # Update position
        position = motor.get_position()

    # Stop
    motor.stop()

def iteration():
    print("iteration entry")

    # Get twin motors
    twins = motor.Twin(motor.portA, motor.portB)

    # Move forward by 50 cm
    move_gradual(twins, -50)

iteration()
