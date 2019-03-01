# This script sets up the environment.
# It sets the in3 port's mode to raw and sets up permissions on value file of GPIO 121.
# Requires sudo permissions.
#
# Author(s):
#   Filip Smola

# Set in3 port's mode to raw
echo "raw" > /sys/class/lego-port/port2/mode

# Set group and permissions to value of GPIO 121 to gpio and 664 (rw-rw-r--)
chown root:gpio /sys/class/gpio/gpio121/value
chmod 664 /sys/class/gpio/gpio121/value

# Turn off
echo 0 >> /sys/class/gpio/gpio121/value
