# Various movement schemes used by the tests.
#
# Authors:
#   Filip Smola

import time
import math

# Gradual movement guide functions (distance progress to maximum speed multiplier - [0,1] -> [0,1])
def sine_guide(x):
    # Return zero outside of supported range
    if x < 0:
        return 0
#    if x > 1:
#        return 0

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
        self.long_distance = 15
        self.poll_t = 0.1

        # run_direct specific
        self.max_dc_long = 70
        self.max_dc_short = 40
        self.min_dc = 20
        self.step_dc = 5

        # run_to_abs_pos specific
        self.max_speed_long = 500
        self.max_speed_short = 250
        self.min_speed = 100
        self.step_speed = 50

    # Move a motor a set linear distance (in cm)
    def move_by(self, motor, distance):
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

    # Move a motor to a position (in cm)
    # Returns the deviation from target position (in cm)
    def move_to(self, motor, position):
        # Note: sign of speed doesn't matter to run_to_abs_pos

        print("Moving %s gradually to %f cm" % (motor.name, position))

        # Pick maximum speed
        is_long = math.fabs(position - self.deg_to_cm(motor.get_position())) >= self.long_distance
        max_speed = self.max_speed_long if (is_long) else self.max_speed_short

        # Convert position to degrees
        angular = self.cm_to_deg(position)

        # Get starting position and distance
        start = motor.get_position()
        distance = math.fabs(angular - start)

        # Skip if no movement required
        if distance == 0:
            print("Distance is zero. No movement required.")
            return self.deg_to_cm(motor.get_position() - angular)

        # Start moving
        motor.run_to_abs_pos(angular, self.min_speed)

        # Adjust speed while the motor is running
        while motor.is_running():
            # Compute guide argument
            d = math.fabs(motor.get_position() - start) / distance

            # Compute desired speed
            desired = max_speed * self.guide(d)

            # Set desired speed as next multiple of step_speed greater than min_speed
            desired = max(math.ceil(desired / self.step_speed) * self.step_speed, self.min_speed)

            # Command motor to move to angular position at desired speed
            motor.run_to_abs_pos(angular, desired)

            # Delay
            time.sleep(self.poll_t)

        # Print message and return error
        print("Done")
        return self.deg_to_cm(motor.get_position() - angular)

    # Convert distance in cm to wheel angle in degrees
    def cm_to_deg(self, cm):
        return cm / self.wheel_circumference * 360

    # Convert wheel angle in degrees to distance in cm
    def deg_to_cm(self, deg):
        return deg / 360 * self.wheel_circumference

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
    def move_by(self, motor, distance):
        # Pick speed
        speed = self.speed_long if (math.fabs(distance) >= self.long_distance) else self.speed_short

        print("Moving %s uniformly over %f cm at speed %d" % (motor.name, distance, speed))

        # Compute distance in wheel angle
        angular = self.cm_to_deg(distance)

        # Run motor for computed distance at set speed and wait to finish
        motor.run_to_rel_pos(angular, speed)
        motor.wait_while('running')

    # Move a motor to a position (in cm)
    # Returns the deviation from target position (in cm)
    def move_to(self, motor, position):
        # Pick speed
        distance = math.fabs(position - self.deg_to_cm(motor.get_position()))
        speed = self.speed_long if (distance >= self.long_distance) else self.speed_short

        print("Moving %s uniformly to %f cm at speed %d" % (motor.name, position, speed))

        # Convert position to degrees
        angular = self.cm_to_deg(position)

        # Command motor to move to angular position at maximum speed
        motor.run_to_abs_pos(angular, speed)
        motor.wait_while('running')

        # Print message and return error
        print("Done")
        return self.deg_to_cm(motor.get_position() - angular)

    # Convert distance in cm to wheel angle in degrees
    def cm_to_deg(self, cm):
        return cm / self.wheel_circumference * 360

    # Convert wheel angle in degrees to distance in cm
    def deg_to_cm(self, deg):
        return deg / 360 * self.wheel_circumference
