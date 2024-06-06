from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))

oled = SSD1306_I2C(128, 64, i2c, 0x3c)
oled.fill(0)
oled.text("Hello NSI", 28, 32)
oled.show()
