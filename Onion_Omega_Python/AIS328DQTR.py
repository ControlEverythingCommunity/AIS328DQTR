# Distributed with a free-will license.
# Use it any way you want, profit or free, provided it fits in the licenses of its associated works.
# AIS328DQTR
# This code is designed to work with the AIS328DQTR_I2CS I2C Mini Module available from ControlEverything.com.
# https://www.controleverything.com/content/Accelorometer?sku=AIS328DQTR_I2CS#tabs-0-product_tabset-2

from OmegaExpansion import onionI2C
import time

# Get I2C bus
i2c = onionI2C.OnionI2C()

# AIS328DQTR address, 0x18(24)
# Select control register1, 0x20(32)
#		0x27(39)	Power ON mode, Data rate selection = 50Hz
#					X, Y, Z-Axis enabled
i2c.writeByte(0x18, 0x20, 0x27)
# AIS328DQTR address, 0x18(24)
# Select control register4, 0x23(35)
#		0x30(48)	Continuous update, Full-scale selection = +/-8G
i2c.writeByte(0x18, 0x23, 0x30)

time.sleep(0.5)

# AIS328DQTR address, 0x18(24)
# Read data back from 0x28(40), 2 bytes
# X-Axis LSB, X-Axis MSB
data0 = i2c.readBytes(0x18, 0x28, 1)
data1 = i2c.readBytes(0x18, 0x29, 1)

# Convert the data
xAccl = data1 * 256 + data0
if xAccl > 32767 :
	xAccl -= 65536

# AIS328DQTR address, 0x18(24)
# Read data back from 0x2A(42), 2 bytes
# Y-Axis LSB, Y-Axis MSB
data0 = i2c.readBytes(0x18, 0x2A, 1)
data1 = i2c.readBytes(0x18, 0x2B, 1)

# Convert the data
yAccl = data1 * 256 + data0
if yAccl > 32767 :
	yAccl -= 65536

# AIS328DQTR address, 0x18(24)
# Read data back from 0x2C(44), 2 bytes
# Z-Axis LSB, Z-Axis MSB
data0 = i2c.readBytes(0x18, 0x2C, 1)
data1 = i2c.readBytes(0x18, 0x2D, 1)

# Convert the data
zAccl = data1 * 256 + data0
if zAccl > 32767 :
	zAccl -= 65536

# Output data to screen
print "Acceleration in X-Axis : %d" %xAccl
print "Acceleration in Y-Axis : %d" %yAccl
print "Acceleration in Z-Axis : %d" %zAccl
