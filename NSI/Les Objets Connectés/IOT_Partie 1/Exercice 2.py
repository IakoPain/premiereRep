from machine import ADC
from time import sleep

adc = ADC(0)

while True:
    valeur=adc.read()
    print(valeur)
    sleep(1)