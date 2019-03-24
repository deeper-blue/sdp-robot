# Production run script
#
# Author(s):
#   Filip Smola

from comms import server
from high_level import hli_implementation
from low_level import arch, platform, grabber, pickup, button

# Instantiate LLI
ar = arch.Arch()
pl = platform.Platform()
gr = grabber.grabber
pi = pickup.Pickup()
bu = button.Button()

# Instantiate HLI
hli = hli_implementation.High_Level_Interface(('A',1), ar, pl, gr, pi, bu)

# Instantiate server
ser = server.Server(hli)

# Run server
ser.run()
