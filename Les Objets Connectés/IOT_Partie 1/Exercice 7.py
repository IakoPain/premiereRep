NBPIXELS=4

from neopixel import NeoPixel
from machine import Pin,ADC
from time import sleep_ms

np = NeoPixel(Pin(14), NBPIXELS)
adc = ADC(0)

LUMIERE_MIN = 300

while True:
    valeur = adc.read()
    print(valeur)
    couleur=(0,0,(valeur-LUMIERE_MIN)//8)
    for n in range(0,NBPIXELS):
        np[n] = couleur
    np.write()
    