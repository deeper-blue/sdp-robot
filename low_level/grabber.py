# Implementation of the Low Level Interface for the Grabber.
#
# Author(s):
#   Filip Smola

import math

from . import config
from . import motor
from . import move

# Notes:
#   - Assumes positive motor direction is moving grabber down.
#   - Two options for up position are at platform and two figures from the board.
#   - Assumes motor starts in the up position.

# Grabber up position in tacho counts down from position at platform
#up_pos = config.grabber_height - (config.board_height + 2 * config.tallest_piece)   # two figures in cm
up_pos = 0  # at platform in cm
up_pos = math.floor(up_pos) # round down

# Grabber down position
down_pos = config.grabber_height - (config.board_height + config.tallest_piece) # in cm
down_pos = math.floor(down_pos) # round down

# Grabber board position
board_pos = config.grabber_height - config.board_height # in cm
board_pos -= 1  # just above board

# Thread Grabber
class Thread:
    # What position the grabber is in (up, down, board)
    position = 'up'
    # Whether the electromagnet is turned on
    on = False
    # Last error in tachos
    last_error = 0
    # Uniform movement scheme
    movement = move.Uniform(config.grabber_circ)

    # Construct a grabber from the attached motor
    def __init__(self, motor):
        # Set motor and reset its position to preconfigured down
        self.motor = motor
        self.motor.set_position(self.movement.cm_to_deg(up_pos))

        # Announce self
        print("Grabber created at %d and controlled by %s" % (self.motor.get_position(), self.motor.name))
        self.print_state()


    # Move grabber into the up position
    def go_up(self):
        # Check not up
        if self.position == 'up' :
            print("Warning: Grabber already up.")
            return

        # Move motor to configured up position
        self.last_error = self.movement.move_to(self.motor, up_pos)

        # Print info and update state
        print("Grabber:\tMoved up (error: %d cm)" % (self.last_error))
        self.position = 'up'

    # Move grabber into the down position
    def go_down(self):
        # Check not down
        if self.position == 'down':
            print("Warning: Grabber already down.")
            return

        # Move motor to configured down position
        self.last_error = self.movement.move_to(self.motor, down_pos)

        # Print info and update state
        print("Grabber:\tMoved down (error: %d cm)" % (self.last_error))
        self.position = 'down'

    # Move grabber to the board
    def go_to_board(self):
        # Check not board
        if self.position == 'board':
            print("Warning: Grabber already at board.")
            return

        # Move motor to configured board position
        self.last_error = self.movement.move_to(self.motor, board_pos)

        # Print info and update state
        print("Grabber:\t Moved to board (error: %d cm)" % (self.last_error))
        self.position = 'board'

    # Turn electromagnet on
    def turn_on(self):
        # Write to GPIO value file
        file = open("/sys/class/gpio/gpio%d/value" % (config.magnet_gpio_no), "w")
        file.write("1")
        file.close()

        # Print info and update state
        print("Grabber:\t Magnet turned off")
        self.on = True

    # Turn electromagnet off
    def turn_off(self):
        # Write to GPIO value file
        file = open("/sys/class/gpio/gpio%d/value" % (config.magnet_gpio_no), "w")
        file.write("0")
        file.close()

        # Print info and update state
        print("Grabber:\t Magnet turned off")
        self.on = False

    # Print state summary
    def print_state(self):
        print("Grabber: position = %s; on = %s" % (self.position, "true" if self.on else "false"))

# Instantiate default object
grabber = Thread(motor.Single(config.grabber_motor_port))
