# An implementation of the LLI for the arch of the robot
#
# Author(s):
#   Filip Smola
#   Jeremy Scott

from . import config
from . import motor
from . import move
from . import time
from ev3dev.ev3 import *

# Dummy accuracy (error added per unit moved)
accuracy = 0.01

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

    # Go to specified cell's column
    def go_to_cell(self, cell):
        # Unpack column
        (column, _) = cell

        # Check for error over threshold
        self.check_error()

        # Compute target and relative positions
        target = config.cell_column_cm(column)
        relative = target - self.position

        # Move the arch by the given amount
        print("Moving Arch by %f from %f to %f" % (relative, self.position, target))
        self.move_arch(-relative)
        self.position += relative
        self.error += accuracy * relative

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
        
    def move_arch(self, dist):
        # Move in the direction and by the amount specified in dist
        self.movement.move(self.twins, dist)

    # Reset self if error is over threshold
    def check_error(self):
        if self.error > threshold:
            print("Arch error is %f cm (threshold: %f cm), resetting..." % (self.error, threshold))
            self.go_to_edge()

    # Print state summary
    def print_state(self):
        print("Arch: position = %f; error = %f" % (self.position, self.error))