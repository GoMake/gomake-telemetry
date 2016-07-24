from sensor import Sensor
import grovepi

# (5 * grovepi.analogRead(0) * 100) / 1024 <--- formula for LM35 sensor
class Sound(Sensor):
	name = 'Sound'
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
			return '0'
		try:	
			analogValue = grovepi.analogRead(self.pin)
			return str(analogValue)
		except (IOError, TypeError) as e:
		    self.logError('Could not read value from sensor')	
		return '0'	

if __name__ == '__main__':
	s = Sound(0)
	sound = s.read()
	print str(sound)
