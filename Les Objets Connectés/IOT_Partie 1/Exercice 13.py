from machine import Pin,I2C,RTC
from time import sleep

rtc = RTC()

#(year, month, day, weekday, hours, minutes, seconds, subseconds)
rtc.datetime((2019, 8, 2, 4,13,55, 0,0)) 

while True:
    horloge=rtc.datetime()
    print(horloge[4],":",horloge[5],":",horloge[6])
    sleep(1)
    