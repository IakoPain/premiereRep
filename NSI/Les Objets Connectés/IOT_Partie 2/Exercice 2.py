import network

# wifi connection station mode
wifi = network.WLAN(network.STA_IF)

# wifi is connected ?
if wifi.isconnected():
    print ("connecté au réseau wifi")
    print(wifi.ifconfig())    
else:
    print (" NON connecté au réseau wifi")