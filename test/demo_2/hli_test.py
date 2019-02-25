# HLI implementation test.
#
# Author(s):
#   Stewart Wilson

from high_level import config
from high_level import hli_implementation
from low_level.dummy import arch, platform, grabber


def run():

    # Instantiate hli
    preset_state = ('L',1)
    hli = hli_implementation.High_Level_Interface(preset_state, arch, platform, grabber)

    # Run experiment 1: Moving piece
    cellA = ('B',2)
    cellB = ('D',4)

    hli.move_piece(cellA, cellB)
    ##### End experiment 1 #####
    print('\n')
    # Run experiment 2: Taking piece
    cellB = ('D',4)
    cellC = ('D',6)
    piece = "white_king"

    hli.take_piece(cellB, cellC, "white_king")
    ##### End experiment 2 #####
    print('\n')
    # Run experiment 3: Castling
    cellA = ('A',5)
    cellB = ('A',1)
    cellC = ('A',7)
    cellD = ('A',6)

    hli.perform_castling_at(cellA, cellB, cellC, cellD)
    ##### End experiment 2 #####
