# Quantitative analysis of Arch: 10 movements from 0 cm to 50 cm and back.
#
# Author(s):
#   Filip Smola

import time
from test.demo_2 import hli_prepare as env

# Reset, centre platform and go to 0
env.hli.reset()
env.pl.centre()
env.ar.move(0)

# Repeat experiment
print("Starting Arch QA")
errors = []
for i in range(0,10):
    time.sleep(2)
    env.ar.move(50)
    errors.append(env.ar.error)
    env.ar.print_state()
    input("Waiting for Enter...")
    env.ar.move(0)

# Print errors
print("Perceived errors: %s cm" % (errors))
