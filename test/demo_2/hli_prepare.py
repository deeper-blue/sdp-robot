# HLI preparation
#
# Author(s):
#   Filip Smola

from high_level import hli_implementation
from low_level import arch, platform, grabber, pickup, button

# Instantiate LLI
ar = arch.Arch()
pl = platform.Platform()
gr = grabber.grabber
pi = pickup.Pickup()
bu = button.Button()

# Instantiate hli
hli = hli_implementation.High_Level_Interface(('L',1), ar, pl, gr, pi, bu)
