from neopixel import NeoPixel
from machine import Pin
from time import sleep_ms

np = NeoPixel(Pin(14), 4)

while True:
    for i in range(0,256,32):
        for j in range(0,256,32):
            for k in range(0,256,32):
                np[0]=(k,j,i)
                np[1]=(k,j,i)
                np[2]=(k,j,i)
                np[3]=(k,j,i)
                np.write()
                sleep_ms(75)