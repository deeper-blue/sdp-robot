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
    movement = move.Gradual(config.platform_circ)

    # Reset position on construction
    def __init__(self):
        self.single.set_position(0)
        self.movement.speed_long = 150

    # Go to specified cell's row
    def go_to_cell(self, cell):
        # Unpack row
        (_, row) = cell

        # Check for error over threshold
        self.check_error()

        # Compute target position
        target = config.cell_row_cm(row)

        # Move the platform to the specified row
        self.move(target)

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
        self.single.set_position(self.movement.cm_to_deg(config.platform_reset_position))

    # Go to centre of top rail
    def centre(self):
        # Get target and compute relative position
        target = config.top_centre

        # Move the platform to the centre
        self.move(target)

    # Move to the target position
    def move(self, target):
        print("Moving Platform from %f to %f" % (self.position, target))
        self.error = self.movement.move_to(self.single, target)
        self.position = target

    # Reset self if error is over threshold
    def check_error(self):
        if self.error > threshold:
            print("Platform error is %f cm (threshold: %f cm), resetting..." % (self.error, threshold))
            self.go_to_edge()

    # Print state summary
    def print_state(self):
        print("Platform: position = %f; error = %f" % (self.position, self.error))
