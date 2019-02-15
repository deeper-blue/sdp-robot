# Dummy implementations of the High Level Interface.
# These implementations only change internal state and print commands to standard output.
# They do not control any hardware.
#
# Author(s):
#   Stewart Wilson

import config

preset_state = ('A', 1)
current_state = ('A', 1)


# Dummy Arch
class High_Level_Interface:

    # Move piece to empty square
    def move_piece(self, cellA, cellB):
        self.move(cellA, cellB)
        self.reset()


    # Move piece in cellA to cellB
    def move(self, cellA, cellB):
        # Pretend
        print("Moving piece at %s to %s" % (cellA, cellB))

    # Go to reset by going to preset state
    def reset(self):
        # Pretend
        print("Moving robot to preset state/cell")

        # Changing state to preset cell
        self.current_state = preset_state


    # Take piece in cellB and replace with one in cellA
    def take_piece(self, cellA, cellB, piece):
        # Get buffer cell for piece
        buffer_cell = config.select_buffer_cell(piece)

        self.move(cellB, buffer_cell)
        self.move(cellA, cellB)
        self.reset()

    # Castling function (May need reworked)
    def perform_castling_at(self, cellA, cellB, cellC, cellD):
        self.move(cellA, cellC)
        self.move(cellB, cellD)
        self.reset()




hli = High_Level_Interface()
testcell = ('B', 2)
testcell1 = ('D', 4)
hli.move_piece(testcell, testcell1)
hli.take_piece(testcell, testcell1, "black_knight0")