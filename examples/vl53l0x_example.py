# Simple demo of the VL53L0X distance sensor.
# This program is meant to be used with a Wireling Pi Hat, and Time of Flight (Distance) Sensor Wireling
# Prints the distance in mm read by the sensor every second
# Adapted from Adafruit example by: Corey Miller for TinyCircuits
# Initialized: 9-10-19
# Last Updated: 12-16-19

import time
import board
import busio
import adafruit_vl53l0x
import tinycircuits_wireling

# Initialize and enable power to Wireling Pi Hat
wireling = tinycircuits_wireling.Wireling()

# Toggle this variable to use the Light Sensor Wireling on a different port (0-3)
port = 0
wireling.selectPort(port)

# Initialize I2C bus and sensor.
i2c = busio.I2C(board.SCL, board.SDA)
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Optionally adjust the measurement timing budget to change speed and accuracy.
# See the example here for more details:
#   https://github.com/pololu/vl53l0x-arduino/blob/master/examples/Single/Single.ino
# For example a higher speed but less accurate timing budget of 20ms:
#vl53.measurement_timing_budget = 20000
# Or a slower but more accurate timing budget of 200ms:
#vl53.measurement_timing_budget = 200000
# The default timing budget is 33ms, a good compromise of speed and accuracy.

# Main loop will read the range and print it every second.
while True:
    print('Range: {0}mm'.format(vl53.range))
    time.sleep(1.0)
