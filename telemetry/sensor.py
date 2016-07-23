import logging

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
			logging.info(self.sensorType + ' Sensor::' + message)
	def logError(self, message):
		if(self.logger and message):
			logging.error(self.sensorType + ' Sensor::' + message)