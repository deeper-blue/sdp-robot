# Implementation of the Low Level Interface for the Grabber.
#
# Author(s):
#   Filip Smola

from . import config
from . import motor

# Notes:
#   - Assumes positive motor direction is moving grabber down.
#   - Two options for up position are at platform and two figures from the board.
#   - Assumes motor starts in the down position.

# Grabber up position in tacho counts down from position at platform
up_pos = config.grabber_height - (config.board_height + 2 * config.tallest_piece)   # two figures in cm
#up_pos = 0  # at platform in cm
up_pos = up_pos / config.grabber_circ * 360 # to degrees

# Grabber down position
down_pos = config.grabber_height - (config.board_height + config.tallest_piece) # in cm
down_pos = down_pos / config.grabber_circ * 360 # to degrees

# Speed in tacho counts per second
speed = 270 # 3/4 rotations per second

# Thread Grabber
class Thread:
    # Whether the grabber is in the up position
    up = False
    # Whether the electromagnet is turned on
    on = False

    # Construct a grabber from the attached motor
    def __init__(self, motor):
        # Set motor and reset its position to preconfigured down
        self.motor = motor
        self.motor.set_position(down_pos)

    # Move grabber into the up position
    def go_up(self):
        # Check not up
        if self.up:
            print("Warning: Grabber already up.")
            return

        # Move motor to configured up position
        self.motor.run_to_abs_pos(up_pos, speed)

        # Print info and update state
        print("Grabber:\tMoved up (error: %f tachos)" % (self.motor.get_position() -  up_pos))
        self.up = True

    # Move grabber into the down position
    def go_down(self):
        # Check not down
        if not self.up:
            print("Warning: Grabber already down.")
            return

        # Move motor to configured down position
        self.motor.run_to_abs_pos(down_pos, speed)

        # Print info and update state
        print("Grabber:\tMoved down (error: %f tachos)" % (self.motor.get_position() -  up_pos))
        self.up = False

    # Turn electromagnet on
    def turn_on(self):
        raise NotImplementedError

    # Turn electromagnet off
    def turn_off(self):
        raise NotImplementedError

    # Print state summary
    def print_state(self):
        print("Grabber: up = %s; on = %s" % ("True" if self.up else "False", "true" if self.on else "false"))

# Instantiate default object
grabber = Thread(motor.Single(config.grabber_motor_port))
