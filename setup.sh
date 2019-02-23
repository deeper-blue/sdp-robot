# This script sets up the environment.
# It sets the in3 port's mode to raw and sets up permissions on value file of GPIO 121.
# Requires sudo permissions.
#
# Author(s):
#   Filip Smola

# Set in3 port's mode to raw
echo "raw" > /sys/class/lego-port/port2/mode

# Set permissions to value of GPIO 121 to 664 (rw-rw-r--)
sudo chmod 664 /sys/class/gpio/gpio121/value
