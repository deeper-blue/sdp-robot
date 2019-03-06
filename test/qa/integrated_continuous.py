# Quantitative analysis of moving piece from A1 to L8 and back continuously until told to stop.
# Waits for input after each piece move.
# Input of "stop" terminates the test and prints the count, anything else starts next move.
#
# Author(s):
#   Filip Smola

import time
from test.demo_2 import hli_prepare as env

# Reset and move piece
env.hli.reset()

# Repeat experiment
print("Starting Integrated Continuous A1<->L8 QA")
forward = True  # A1->L8 iff true
comm = ""
i = 0
while comm != "stop":
    i += 1;

    if forward:
        env.hli.move_piece(('A',1),('L',8))
        forward = False
    else:
        env.hli.move_piece(('L',8),('A',1))
        forward = True

    comm = input("Input stop to terminate, anything else to continue.")

print("Count: %d" % (i))
