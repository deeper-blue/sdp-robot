# HLI preparation
#
# Author(s):
#   Filip Smola

from high_level import hli_implementation
from low_level import arch, platform, grabber

# Instantiate LLI
ar = arch.Arch()
pl = platform.Platform()
gr = grabber.grabber

# Instantiate hli
hli = hli_implementation.High_Level_Interface(('L',1), ar, pl, gr)
