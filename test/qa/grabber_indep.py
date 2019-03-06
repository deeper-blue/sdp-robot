# Quantitative analysis of Grabber: 10 movements from up to down and back.
#
# Author(s):
#   Filip Smola

import time
from test.demo_2 import hli_prepare as env

def run():
    # Reset and move to up
    env.hli.reset()
    env.gr.go_up()

    # Repeat experiment
    print("Starting Grabber QA")
    errors = []
    for i in range(0,10):
        time.sleep(2)
        env.gr.go_down()
        errors.append(env.gr.last_error)
        env.gr.print_state()
        input("Waiting for Enter...")
        env.gr.go_up()

    # Print errors
    print("Perceived errors: %s cm" % (errors))
