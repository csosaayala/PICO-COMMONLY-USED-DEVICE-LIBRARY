from machine import I2C
from sh1106 import SH1106_I2C

i2c = I2C(0)

oled = SH1106_I2C(128,64,i2c)

oled.rotate(True)
oled.fill(0)
oled.text("Man is evil", 64, 32)
oled.show()