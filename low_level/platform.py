# An implementation of the LLI for the platform of the robot
#
# Author(s):
#   Filip Smola
#   Jeremy Scott

from . import config
from . import motor
from . import move
import time
from ev3dev.ev3 import *

# Dummy accuracy (error added per unit moved)
accuracy = 0.01

# Error threshold (in cm)
threshold = 10.0

# Implemented platform
class Platform:
    # Internal position in cm (along top rail)
    position = 0
    # Expected error in cm (internal - real)
    error = 0
    # Get single motor
    single = motor.Single(config.platform_motor)
    # Prepare movement
    movement = move.Gradual(config.wheel_circ)

    # Go to specified cell's row
    def go_to_cell(self, cell):
        # Unpack row
        (_, row) = cell

        # Check for error over threshold
        self.check_error()

        # Compute target and relative positions
        target = config.cell_row_cm(row)
        relative = target - self.position

        # Move the platform to the specified row
        print("Moving Platform by %f from %f to %f" % (relative, self.position, target))
        self.move_platform(relative)
        self.position += relative
        self.error += accuracy * relative

    # Go to minimum row edge and reset
    def go_to_edge(self):
        # Send the platform to the reset end, to set the error to 0
        print("Moving Platform in negative direction until reset button is hit")

        ts1 = TouchSensor(config.touch_sensor_platform)

        # Platform moves until sensor is pressed
        while not ts1.is_pressed:
            self.single.run_direct(-20)
            time.sleep(0.01)

        self.single.stop()
        print("End reached!")

        self.position = config.platform_reset_position
        self.error = 0

    # Go to centre of top rail
    def centre(self):
        # Get target and compute relative position
        target = config.top_centre
        relative = target - self.position

        # Move the platform to the centre
        print("Moving Platform by %f from %f to %f - the top rail centre" % (relative, self.position, target))
        self.move_platform(relative)
        self.position += relative
        self.error += accuracy * relative

    def move_platform(self, dist):
        # Move in the direction and by the amount specified in dist
        self.movement.move(self.single, dist)

    # Reset self if error is over threshold
    def check_error(self):
        if self.error > threshold:
            print("Platform error is %f cm (threshold: %f cm), resetting..." % (self.error, threshold))
            self.go_to_edge()

    # Print state summary
    def print_state(self):
        print("Platform: position = %f; error = %f" % (self.position, self.error))
