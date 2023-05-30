import network
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)

i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)

# wait for connection
while not wifi.isconnected():
    pass

# wifi is connected ?
if wifi.isconnected():
    print(wifi.ifconfig())