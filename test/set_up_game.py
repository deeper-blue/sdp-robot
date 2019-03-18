# Moves all of buffer to board.
#
# Author(s):
#   Filip Smola

from test.demo_2 import hli_prepare as env

cols = 'ABCDEFGHIJKL'

env.hli.reset()

# For each starting position
for col in 'ABCDEFGH':
    for row in [1,2,7,8]:
        starting = (col,row)
        buffer = env.hli_implementation.config.buffer_cell(starting)
        buffer = (cols[buffer[0]], buffer[1] + 1)

        env.hli.move_piece(buffer, starting)
