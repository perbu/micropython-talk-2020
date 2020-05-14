from machine import I2C, Pin
i2c = I2C(sda=Pin(21), scl=Pin(22))
print(i2c.scan())
