import smbus
import RPi.GPIO as GPIO
from grove_i2c_barometic_sensor_BMP180 import BMP085
from sensor import Sensor

class Barometer(Sensor):
        name="Barometer"
	def __init__(self, logger=None):
                Sensor.__init__(self, self.name, logger)
		self.bmp = BMP085(0x77, 1)
		self.initSMBus()
	def initSMBus(self):
		rev = GPIO.RPI_REVISION
		if rev == 2 or rev == 3:
			bus = smbus.SMBus(1)
		else:
			bus = smbus.SMBus(0)
	def read(self):
		pressure = self.bmp.readPressure()
		return "%.2f" % (pressure / 100.0)
	def readTemperature(self):
		temperature = self.bmp.readTemperature()
		return "%.2f" % (temperature)
	def readAltitude(self):
		pressure = self.bmp.readPressure()
		altitude = self.bmp.readAltitude(pressure)
		return "%.2f" % (altitude)		

if __name__ == '__main__':
        b = Barometer()
        print b.read()
