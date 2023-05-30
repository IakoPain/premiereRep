from neopixel import NeoPixel
from machine import Pin

np = NeoPixel(Pin(14), 4)
np[0] = (255,0, 0)
np[1] = (0, 255, 0) 
np[2] = (0, 0, 255)
np[3] = (255, 255, 0)

np.write()