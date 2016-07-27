from sensor import Sensor
import grovepi

# (5 * grovepi.analogRead(0) * 100) / 1024 <--- formula for LM35 sensor
class Temperature(Sensor):
	name = 'Temperature'
	def __init__(self, pin, logger=None):
		Sensor.__init__(self, self.name, logger)
		self.pin = pin
		self.connect()
	def connect(self):
		if(not isinstance(self.pin, int)):
			self.validPin = False
		else:
			self.validPin = True
		grovepi.pinMode(self.pin, "INPUT")
	def read(self):
		if(not self.validPin):
			self.logError('No valid pin provided')
			return 0
		try:	
			analogValue = grovepi.analogRead(self.pin)
			temperature = (5.0 * analogValue * 100.0) / 1024
			return temperature
		except (IOError, TypeError) as e:
		    self.logError('Could not read value from sensor')	
		return 0	

if __name__ == '__main__':
	t = Temperature(0)
	temp = t.read()
	print str(temp)
