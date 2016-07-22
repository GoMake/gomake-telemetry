class Sensor(object):
	sensorType = '__undefinedsensor__'
	def __init__(self, type, logger=None):
		self.sensorType = type
		self.logger = logger
	def read(self):
		pass
	def getType(self):
		return self.sensorType
	def logMessage(self, message):
		if(self.logger and message):
			self.logger.info(self.sensorType + ' Sensor::' + message)
	def logError(self, message):
		if(self.logger and message):
			self.logger.error(self.sensorType + ' Sensor::' + message)