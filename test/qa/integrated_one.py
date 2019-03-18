# Quantitative analysis of moving piece from A1 to L8 (just that direction) 10 times with piece centering by hand after each trial.
#
# Author(s):
#   Filip Smola

import time
from test.demo_2 import hli_prepare as env

def run():
    # Reset and move piece
    env.hli.reset()

    # Repeat experiment
    print("Starting Integrated A1->L8 QA")
    for i in range(0,10):
        time.sleep(2)
        env.hli.move_piece(('A',1),('L',8))
        input("Waiting for Enter...")
