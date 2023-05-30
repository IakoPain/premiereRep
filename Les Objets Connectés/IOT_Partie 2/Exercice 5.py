import network
import urequests
import ujson
import utime

# user data
url = "http://worldtimeapi.org/api/timezone/Europe/Paris" 

# initialization

response = urequests.get(url)
    
if response.status_code == 200:
    worldtime = ujson.loads(response.text)
    print(type(worldtime))
    print(worldtime.keys())
    print(worldtime)
  
else:
    print("Pas de réponse")
