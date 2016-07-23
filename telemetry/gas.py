from sensor import Sensor
import grovepi

# (5 * grovepi.analogRead(0) * 100) / 1024 <--- formula for LM35 sensor
class Gas(Sensor):
	name = 'Gas'
	calibrationSampleSize = 100
	R0 = 1
	def __init__(self, pin, logger=None):
		Sensor.__init__(self, self.name, logger)
		self.pin = pin
		self.connect()
		self.calibrate()
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
			sensorVoltage = analogValue / 1024 * 5.0
			RS = (5.0 - sensorVoltage) / sensorVoltage
			return str(RS / self.R0)
		except (IOError, TypeError) as e:
		    self.logError('Could not read value from sensor')	
		return '0'	
	def calibrate(self):
		for x in range(1,self.calibrationSampleSize):
			analogValue += grovepi.analogRead(self.pin)
		analogValue /= self.calibrationSampleSize
		sensorVoltage = analogValue / 1024 * 5.0
		RS = (5.0 - sensorVoltage) / sensorVoltage
		self.R0 = RS / 9.8
if __name__ == '__main__':
	s = Sound(0)
	sound = s.read()
	print str(sound)
