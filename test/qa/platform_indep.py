# Quantitative analysis of Platform: 10 movements from 0 cm to 30 cm and back.
#
# Author(s):
#   Filip Smola

import time
from test.demo_2 import hli_prepare as env

def run():
    # Reset and move to 0
    env.hli.reset()
    env.pl.move(0)

    # Repeat experiment
    print("Starting Platform QA")
    errors = []
    for i in range(0,10):
        time.sleep(2)
        env.pl.move(30)
        errors.append(env.pl.error)
        env.pl.print_state()
        input("Waiting for Enter...")
        env.pl.move(0)

    # Print errors
    print("Perceived errors: %s cm" % (errors))
