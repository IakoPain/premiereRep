from machine import ADC,Pin
from time import sleep

adc = ADC(0)
led = Pin(0,Pin.OUT)
while True:
    valeur=adc.read()
    if valeur <400:
        led.on()
    else:
        led.off()
    