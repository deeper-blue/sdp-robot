# An implementation of the LLI for the arch of the robot
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

# Implemented Arch
class Arch:
    # Internal position in cm (along bottom rail)
    position = 0
    # Expected error in cm (internal - real)
    error = 0
    # Get twin motors
    twins = motor.Twin(config.left_arch_motor, config.right_arch_motor)
    # Prepare movement
    movement = move.Gradual(config.wheel_circ)

    # Reset position on construction
    def __init__(self):
        self.twins.set_position(0)

    # Go to specified cell's column
    def go_to_cell(self, cell):
        # Unpack column
        (column, _) = cell

        # Check for error over threshold
        self.check_error()

        # Compute target position
        target = config.cell_column_cm(column)

        # Move the arch by the given amount
        self.move(target)

    # Go to buffer-side edge and reset
    def go_to_edge(self):
        print("Moving Arch in positive direction until reset button is hit")

        ts2 = TouchSensor(config.touch_sensor_arch)

        # Move along the rail until sensor is pressed
        while not ts2.is_pressed:
            self.twins.run_direct(-20)
            time.sleep(0.01)

        self.twins.stop()
        print("End reached!")

        self.position = config.arch_reset_position
        self.error = 0
        self.twins.set_position(-1 * self.movement.cm_to_deg(config.arch_reset_position))

    # Move to the target position
    def move(self, target):
        print("Moving Arch from %f to %f" % (self.position, target))
        self.error = self.movement.move_to(self.twins, -1 * target)
        self.position = target

    # Reset self if error is over threshold
    def check_error(self):
        if self.error > threshold:
            print("Arch error is %f cm (threshold: %f cm), resetting..." % (self.error, threshold))
            self.go_to_edge()

    # Print state summary
    def print_state(self):
        print("Arch: position = %f; error = %f" % (self.position, self.error))
