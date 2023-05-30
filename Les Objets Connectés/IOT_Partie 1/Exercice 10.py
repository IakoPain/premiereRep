HAUTEUR=0
LARGEUR=0
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)


while True:
    for n in range(0,128):
        if n < 64:
            HAUTEUR += 1
        else:
            HAUTEUR -= 1
            
        oled.fill(0)
        oled.text("Hello NSI", 28, HAUTEUR)
        oled.show()
    