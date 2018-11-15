import Adafruit_DHT


class Sensor:
    def __init__(self):
        self.pin = 4
        self.sensor = Adafruit_DHT.DHT22
        
    def get_temp(self):
        humidity, temp = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return temp* 9/5.0 +32
    
    def get_humidity(self):
        humidity, temp = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return humidity

    
    
