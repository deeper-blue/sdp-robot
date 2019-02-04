# Runs the motors uniformly first for 25 cm forward and back, then for 5 cm.
# Used to test uniform movement scheme and how it adapts to long and short distances.
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

    def run_to_rel_pos(self, position, speed):
        self.motorA.run_to_rel_pos(position_sp = position, speed_sp = speed)
        self.motorB.run_to_rel_pos(position_sp = position, speed_sp = speed)

    def stop(self):
        self.motorA.stop()
        self.motorB.stop()

# Maximum and minimum speed (in %)
max_v_long = 70
max_v_short = 40

# Wheel circumference
circ = 12.9 # in cm

# Distance considered long (in degrees)
long_distance = 15 / circ * 360

# Move the motor uniformly by relative distance (in cm)
#TODO support other than TwinMotors
def move_uniform(motor, rel_dist):
    print("move_uniform entry")

    # Compute target rotational distance (in degrees)
    rel_pos = rel_dist / circ * 360

    # Pick speed
    max_v = max_v_long if (target_distance >= long_distance) else max_v_short

    # Run motor for computed distance at max speed
    motor.run_to_rel_pos(rel_pos, max_v)

def iteration():
    print("iteration entry")

    # Get motors and twin them
    motorA = ev3.LargeMotor('outA')
    motorA.connected
    motorB = ev3.LargeMotor('outB')
    motorB.connected
    twins = TwinMotors(motorA, motorB)

    # Move forward by 25 cm and back
    move_uniform(twins, -25)
    move_uniform(twins, 25)

    # Move forward by 5 cm and back
    move_uniform(twins, -5)
    move_uniform(twins, 5)

iteration()
