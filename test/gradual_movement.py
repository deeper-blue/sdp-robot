# Runs the motors gradually for 25 cm forward and back.
# Used to test gradual movement scheme.
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
max_v = 30
min_v = 10

# Valid speeds set (multiples of 5 from min_v to max_v)
# Note: assuming this set is in increasing order
valid_speeds = [z for z in range(min_v,max_v + 1) if z%5 == 0]

# Wheel circumference
circ = 12.9 # in cm

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
        desired = - math.fabs(- (2 * max_v / rel_dist) * d + max_v) + max_v

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
    motorB = ev3.LargeMotor('outB')
    motorB.connected
    twins = TwinMotors(motorA, motorB)

    # Move forward by 25 cm and back
    move_gradual(twins, -25)
    move_gradual(twins, 25)

iteration()
