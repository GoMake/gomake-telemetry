import signal
from sensor import Sensor
import grovepi

# (5 * grovepi.analogRead(0) * 100) / 1024 <--- formula for LM35 sensor
class Button(Sensor):
	name = 'Button'
	def __init__(self, pin, logger=None):
		Sensor.__init__(self, self.name, logger)
		self.pin = pin
		self.connect()
	def connect(self):
		grovepi.pinMode(self.pin, "INPUT")
	def read(self):
		try:
			buttonPressed = grovepi.digitalRead(self.pin)
			return str(buttonPressed)
		except (IOError, TypeError) as e:
		    self.logError('Could not read value from sensor')	
		return '0'	
	def handleReadError(self):
		pass
if __name__ == '__main__':
	b = Button(3)
	buttonPressed = s.read()
	print str(sound)
