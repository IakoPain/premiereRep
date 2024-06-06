from onewire import OneWire
from ds18x20 import DS18X20
from machine import Pin,I2C
from ssd1306 import SSD1306_I2C
from time import sleep_ms
import sys


i2c = I2C(scl=Pin(5), sda=Pin(4))
oled = SSD1306_I2C(128, 64, i2c, 0x3c)
bus = OneWire(Pin(12))
ds = DS18X20(bus)
capteur_temperature = ds.scan()
    
while True:
    try:
        ds.convert_temp()       
        sleep_ms(750)
        temp_celsius = ds.read_temp(capteur_temperature[0])
        oled.fill(0)
        oled.text(str(temp_celsius),0,20)
        oled.show()
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        sys.exit()