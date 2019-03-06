# Quantitative analysis of Grabber: picking a piece up and putting it back down in the same square 10 times.
# Performed at A1.
#
# Author(s):
#   Filip Smola

import time
from test.demo_2 import hli_prepare as env

def run():
    # Reset and move to up
    env.hli.reset()
    env.pl.centre()
    env.hli.go_to_cell(('A',1))

    # Repeat experiment
    print("Starting Grabber in-place QA")
    for i in range(0,10):
        time.sleep(2)
        env.hli.pick_up()
        env.hli.put_down()
        input("Waiting for Enter...")
