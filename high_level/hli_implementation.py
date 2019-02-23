# Implementations of the High Level Interface.
# Implementation used to with low level dummy implementation
#
# Author(s):
#   Stewart Wilson

from . import config
from low_level.dummy import arch, platform, grabber

preset_state = ('L', 1)


# Dummy Arch
class High_Level_Interface:

    def __init__(self, current_state, arch, platform, grabber):
        self.current_state = current_state
        self.arch = arch
        self.platform = platform
        self.grabber = grabber

    def convert_cell(self, cell):
        return (ord(cell[0]) - 65, cell[1] - 1)

    # Move piece to empty square
    def move_piece(self, cellA, cellB):
        self.move(cellA, cellB)
        self.reset()


    # Move piece in cellA to cellB
    def move(self, cellA, cellB):

        print("Moving piece at %s to %s\n" % (cellA, cellB))

        cellA = self.convert_cell(cellA)
        cellB = self.convert_cell(cellB)

        # Move to cellA
        self.arch.go_to_cell(cellA)
        self.platform.go_to_cell(cellA)

        # Pick up piece at cellA
        self.grabber.go_down()
        self.grabber.turn_on()
        self.grabber.go_up()

        # Move to cellB
        self.arch.go_to_cell(cellB)
        self.platform.go_to_cell(cellB)

        # Place piece at cellB
        self.grabber.go_down()
        self.grabber.turn_off()
        self.grabber.go_up()


    # Go to reset by going to preset state
    def reset(self):

        print("Moving robot to preset state/cell")

        # Centre platform and go to preset/reset position
        self.platform.centre()
        self.arch.go_to_edge()
        self.platform.go_to_edge()

        # Changing state to preset cell
        self.current_state = preset_state


    # Take piece in cellB and replace with one in cellA
    def take_piece(self, cellA, cellB, piece):
        # Get buffer cell for piece
        buffer_cell = config.buffer_cells[piece]

        print("Taking piece, %s, at %s with piece at %s\n" % (piece, cellB, cellA))
        self.move(cellB, buffer_cell)
        self.move(cellA, cellB)
        self.reset()

    # Castling function (May need reworked)
    def perform_castling_at(self, cellA, cellB, cellC, cellD):

        print("Peforming Castling at %s and %s\n" % (cellA, cellB))

        self.move(cellA, cellC)
        self.move(cellB, cellD)
        self.reset()




hli = High_Level_Interface(preset_state, arch, platform, grabber)
