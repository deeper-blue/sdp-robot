# Various movement schemes used by the tests.
#
# Authors:
#   Filip Smola

#TODO use motor.count_per_rot instead of constant 360

import time
import math

# Gradual movement guide functions (distance progress to maximum speed multiplier - [0,1] -> [0,1])
def sine_guide(x):
    # Return zero outside of supported range
    if x < 0:
        return 0
    if x > 1:
        return 0

    return math.sin(math.pi * x)

# Gradual movement with speed guided by a function
#
# Parameters:
#   wheel_circumference - Wheel circumference in cm
#   guide - Guide function (with arguments target and current distance); default sine_guide
#   max_dc_long - Maximum duty cycle; default 70
#   max_dc_short - Maximum duty cycle on distances considered short; default 40
#   long_distance - Least linear distance considere long in cm; default 15
#   min_dc - Minimum duty cycle; default 20
#   step_dc - Duty cycle step; default 5
#   poll_t - Position polling perion in seconds; default 0.1
class Gradual:
    # Construct gradual movement from wheel circumference and default values
    def __init__(self, wheel_circumference):
        self.wheel_circumference = wheel_circumference
        self.guide = sine_guide
        self.max_dc_long = 70
        self.max_dc_short = 40
        self.long_distance = 15
        self.min_dc = 20
        self.step_dc = 5
        self.poll_t = 0.1

    # Move a motor a set linear distance (in cm)
    def move(self, motor, distance):
        print("Moving %s gradually over %f cm" % (motor.name, distance))

        # Skip if zero distance
        if distance == 0:
            print("Done")
            return

        # Extract direction
        direction = math.copysign(1.0, distance)
        distance = math.fabs(distance)

        # Pick maximum duty cycle
        max_dc = self.max_dc_long if (distance >= self.long_distance) else self.max_dc_short

        # Compute distance in wheel angle
        angular = self.cm_to_deg(distance)

        # Get current position
        start = motor.get_position()

        # Adjust duty cycle until at least distance far from start
        position = start
        while math.fabs(position - start) < angular:
            # Compute angular distance from start
            d = math.fabs(position - start)

            # Normalize current distance by target total
            d = d / angular

            # Compute desired duty cycle
            desired = max_dc * self.guide(d)

            # Set desired speed as the next multiple of step_dc greater than min_dc
            desired = max(math.ceil(desired / self.step_dc) * self.step_dc, self.min_dc)

            # Reintroduce direction
            desired = direction * desired

            # Set desired speed
            motor.run_direct(desired)

            # Delay
            time.sleep(self.poll_t)

            # Update position
            position = motor.get_position()

        # Stop
        motor.stop()

        print("Done")

    # Convert distance in cm to wheel angle in degrees
    def cm_to_deg(self, cm):
        return cm / self.wheel_circumference * 360

# Uniform movement with constant speed
#
# Parameters:
#   wheel_circumference - Wheel circumference in cm
#   speed_long - Speed on distances considered long; default 300
#   speed_short - Speed on distances considered short; default 100
#   long_distance - Least linear distance considere long in cm; default 15
class Uniform:
    # Construct uniform movement from wheel circumference and default values
    def __init__(self, wheel_circumference):
        self.wheel_circumference = wheel_circumference
        self.speed_long = 300
        self.speed_short = 100
        self.long_distance = 15

    # Move a motor a set linear distance (in cm)
    def move(self, motor, distance):
        # Pick speed
        speed = self.speed_long if (distance >= self.long_distance) else self.speed_short

        print("Moving %s uniformly over %f cm at speed %d" % (motor.name, distance, speed))

        # Compute distance in wheel angle
        angular = self.cm_to_deg(distance)

        # Run motor for computed distance at set speed and wait to finish
        motor.run_to_rel_pos(angular, speed)
        motor.wait_while('running')

    # Convert distance in cm to wheel angle in degrees
    def cm_to_deg(self, cm):
        return cm / self.wheel_circumference * 360
