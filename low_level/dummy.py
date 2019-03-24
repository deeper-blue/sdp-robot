# Dummy implementations of the Low Level Interface.
# These implementations only change internal state and print commands to standard output.
# They do not control any hardware.
#
# Author(s):
#   Filip Smola

from . import config

# Dummy accuracy (error added per unit moved)
accuracy = 0.01

# Error threshold (in cm)
threshold = 10.0

# Pickup sensor state
pickup_present = False

# Dummy Arch
class Arch:
    # Internal position in cm (along bottom rail)
    position = 0
    # Expected error in cm (internal - real)
    error = 0

    # Go to specified cell's column
    def go_to_cell(self, cell):
        # Unpack column
        (column, _) = cell

        # Check for error over threshold
        self.check_error()

        # Compute target and relative positions
        target = config.cell_column_cm(column)
        relative = target - self.position

        # Pretend
        print("Moving Arch by %f from %f to %f" % (relative, self.position, target))
        self.position += relative
        self.error += accuracy * relative

    # Go to buffer-side edge and reset
    def go_to_edge(self):
        # Pretend
        print("Moving Arch in positive direction until reset button is hit")
        self.position = config.arch_reset_position
        self.error = 0

    # Reset self if error is over threshold
    def check_error(self):
        if self.error > threshold:
            print("Arch error is %f cm (threshold: %f cm), resetting..." % (self.error, threshold))
            self.go_to_edge()


    # Print state summary
    def print_state(self):
        print("Dummy Arch: position = %f; error = %f" % (self.position, self.error))

# Dummy Platform
class Platform:
    # Internal position in cm (along top rail)
    position = 0
    # Expected error in cm (internal - real)
    error = 0

    # Go to specified cell's row
    def go_to_cell(self, cell):
        # Unpack row
        (_, row) = cell

        # Check for error over threshold
        self.check_error()

        # Compute target and relative positions
        target = config.cell_row_cm(column)
        relative = target - self.position

        # Pretend
        print("Moving Platform by %f from %f to %f" % (relative, self.position, target))
        self.position += relative
        self.error += accuracy * relative

    # Go to minimum row edge and reset
    def go_to_edge(self):
        # Pretend
        print("Moving Platform in negative direction until reset button is hit")
        self.position = config.platform_reset_position
        self.error = 0

    # Go to centre of top rail
    def centre(self):
        # Get target and compute relative position
        target = config.top_centre
        relative = target - self.position

        # Pretend
        print("Moving Platform by %f from %f to %f - the top rail centre" % (relative, self.position, target))
        self.position += relative
        self.error += accuracy * relative

    # Reset self if error is over threshold
    def check_error(self):
        if self.error > threshold:
            print("Platform error is %f cm (threshold: %f cm), resetting..." % (self.error, threshold))
            self.go_to_edge()

    # Print state summary
    def print_state(self):
        print("Dummy Platform: position = %f; error = %f" % (self.position, self.error))

# Dummy Grabber
class Grabber:
    # What position the grabber is in (up, down, board)
    position = 'up'
    # Whether the electromagnet is turned on
    on = False

    # Move grabber into the up position
    def go_up(self):
        # Check not up
        if self.position == 'up':
            print("Warning: Grabber already up.")
            return

        # Pretend
        print("Moving Grabber up.")
        self.position = 'up'

    # Move grabber into the down position
    def go_down(self, piece = 'default', adjust = 0):
        # Check not down
        if self.position == 'down':
            print("Warning: Grabber already down.")
            return

        # Pretend
        print("Moving Grabber down.")
        self.position = 'down'

    # Move grabber to the board
    def go_to_board(self):
        # Check not board
        if self.position == 'board':
            print("Warning: Grabber already at board.")
            return

        # Print info and update state
        print("Grabber:\t Moved to board (error: %d cm)" % (self.last_error))
        self.position = 'board'

    # Turn electromagnet on
    def turn_on(self):
        # Pretend
        print("Turning Grabber electromagnet on.")
        self.on = True

    # Turn electromagnet off
    def turn_off(self):
        # Pretend
        print("Turning Grabber electromagnet off.")
        self.on = False

    # Print state summary
    def print_state(self):
        print("Dummy Grabber: position = %s; on = %s" % (self.position, "true" if self.on else "false"))

# Dummy pickup sensor
class Pickup:
    def present(self):
        return True

    def absent(self):
        return True

# Dummy resume button
class Button:
    def pressed(self):
        return True

# Instantiate the component objects
arch = Arch()
platform = Platform()
grabber = Grabber()
pickup = Pickup()
button = Button()
