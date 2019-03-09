# Starts the server with a dummy HLI.
#
# Author(s):
#   Filip Smola

from comms import server
from high_level import dummy

# Instantiate HLI
hli = dummy.High_Level_Interface()

# Instantiate server
ser = server.Server(hli)

# Run server
ser.run()
