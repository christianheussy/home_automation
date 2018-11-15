##from utils.relay import Relay
from utils.sensor import Sensor
import time
import sqlite3
import datetime
import RPi.GPIO as GPIO

conn = sqlite3.connect('Home_Automation.db')
c = conn.cursor()

Relay_channel = [17]
GPIO.setmode(GPIO.BCM)
GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.LOW)


def setup():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Relay_channel, GPIO.OUT, initial=GPIO.LOW)


##relay = Relay()
sensor = Sensor()

low_threshold = 70
high_threshold = 78

unix = time.time()
date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

status = "False"
local = "Anders Bedroom"

while True:
    
    temp = sensor.get_temp()
    humidity = sensor.get_humidity()
    
    if temp < low_threshold:
        GPIO.output(Relay_channel, GPIO.LOW)
       
        status = "True"
    if temp > high_threshold:
        GPIO.output(Relay_channel, GPIO.HIGH)
        
        status ="False"
        
    
    
    c.execute("INSERT INTO Anders_Room_Temp (unix, datestamp, local, status, temp, humid) VALUES (?, ?, ?, ?, ?, ?)",
              (unix, date, local, status, temp, humidity))
    conn.commit()
    
    print(status, ": ",temp)
    
    time.sleep(1)
   