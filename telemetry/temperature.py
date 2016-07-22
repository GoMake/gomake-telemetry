from sensor import Sensor
import grovepi

# (5 * grovepi.analogRead(0) * 100) / 1024 <--- formula for LM35 sensor
class Temperature(Sensor):
	name = 'Temperature'
	def __init__(self, pin, logger=None):
		Sensor.__init__(self, self.name, logger)
		self.connect()
	def connect(self):
		grovepi.pinMode(pin, "INPUT")
	def read(self):
		try:	
			analogValue = grovepi.analogRead(0)
			temperature = (5.0 * analogValue * 100.0) / 1024
		except (IOError, TypeError) as e:
		print("Error")			

if __name__ == '__main__':
	t = Temperature()