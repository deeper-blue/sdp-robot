# Runs the motors gradually first for 25 cm forward and back, then for 5 cm.
# Used to test gradual movement scheme and how it adapts to long and short distances.
#
# Authors:
#   Filip Smola

import ev3dev.ev3 as ev3
import time
import math

# Abstraction of two motors to be moved the same (motorA is the Main)
class TwinMotors:
    def __init__(self, motorA, motorB):
        self.motorA = motorA
        self.motorB = motorB

    def get_position(self):
        return self.motorA.position

    def run_direct(self, duty_cycle):
        self.motorA.run_direct(duty_cycle_sp = duty_cycle)
        self.motorB.run_direct(duty_cycle_sp = duty_cycle)

    def stop(self):
        self.motorA.stop()
        self.motorB.stop()

# Position polling delay (in s)
poll_t = 0.1

# Maximum and minimum speed (in %)
max_v_long = 70
max_v_short = 40
min_v = 20

# Wheel circumference
circ = 12.9 # in cm

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
#TODO support other than TwinMotors
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

    # Get motors and twin them
    motorA = ev3.LargeMotor('outA')
    motorA.connected
    motorA.stop_action = motorA.STOP_ACTION_BRAKE
    motorB = ev3.LargeMotor('outB')
    motorB.connected
    motorA.stop_action = motorA.STOP_ACTION_BRAKE
    twins = TwinMotors(motorA, motorB)

    # Move forward by 25 cm and back
    move_gradual(twins, -58)
    move_gradual(twins, 58)

    # Move forward by 5 cm and back
    move_gradual(twins, -5)
    move_gradual(twins, 5)

iteration()
