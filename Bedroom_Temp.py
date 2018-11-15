import sys

import time
from decimal import Decimal
import random
import datetime
import sqlite3
import Adafruit_DHT

conn = sqlite3.connect('Home_Automation.db')
c = conn.cursor()

local = "Anders Bedroom"
ts = 0
pin = 4


sensor = Adafruit_DHT.DHT22
##

unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))


def Monitor_Anders_Bedroom_Condition(temp, humidity):
    ## variable correction, conversion
    temp = temp* 9/5.0 +32
    #temp = Decimal(temp) 
    #humidity = Decimal(humidity)
    temp= round(temp,2) 
    humidity= round(humidity, 2)
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    
    ## BLUE
    if temp in range(70, 75) and humidity > 70:
        status = "BLUE"
        BreakHourInterval = 6
    elif temp <= 80 and humidity <= 80:
        status = "BLUE"
        BreakHourInterval = 8
    
    c.execute("INSERT INTO Anders_Room_Temp (unix, datestamp, local, status, temp, humid) VALUES (?, ?, ?, ?, ?, ?)",
              (unix, date, local, status, temp, humidity))
    conn.commit()
    print(status)
    print("Temp: ", temp)
    print("Humidity: ", humidity)
    print("@: ", date, " Pacific Std")
    print("")
   
try: 
    while True:
        humidity, temp = Adafruit_DHT.read_retry(sensor, pin)
        Monitor_Anders_Bedroom_Condition(temp, humidity)
        time.sleep(60)
except KeyboardInterrupt:
    pass
##
##while True:
##    print(" The temp is: ",temp, " and humidity is: ", humidity)
##    print(ts, "  ", i)
##    time.sleep()
##    print("")