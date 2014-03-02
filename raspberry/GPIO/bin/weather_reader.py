import sys
import requests
import re
import os

madrid_url='http://www.accuweather.com/en/es/madrid/308526/weather-forecast/308526'

TEMP_REGEX = re.compile('class="temp">([^<])+')

req = requests.get(madrid_url)

data = req.text


temp = int(re.findall(TEMP_REGEX,data)[0])

print "TEMPERATURA: %s" % temp

if temp<3:
    os.system("python led_controller.py 1")
else:
    os.system("python led_controller.py 0")
