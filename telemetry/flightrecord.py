import logging
import json

class FlightRecord():
	def __init__(self, timestamp, coordinates, sensorValues):
		self.timestamp = timestamp
		self.coordinates = coordinates
		self.sensorValues = sensorValues
	def getDatabaseFormat(self):
		"""
		timestamp TEXT, lat TEXT, long TEXT, alt TEXT, sensors TEXT
		"""
		flightRecord = {}
		flightRecord['timestamp'] = self.timestamp or ''
		flightRecord['lat'] = self.coordinates['latitude'] or ''
		flightRecord['long'] = self.coordinates['longitude'] or ''
		flightRecord['alt'] = self.coordinates['altitude'] or ''
		flightRecord['sensors'] = json.dumps(self.sensorValues) or '{}'

	def getLogFormat(self):
		logStringArray = []
		logStringArray.append(self.coordinates['latitude'] or '')
		logStringArray.append(self.coordinates['longitude'] or '')
		logStringArray.append(self.coordinates['altitude'] or '')
		logStringArray.append(self.sensorValues['Temperature'] or '')
		logStringArray.append(self.sensorValues['Sound'] or '')
		logStringArray.append(self.sensorValues['Gas'] or '')
		return ','.join(logStringArray)
		
	def getSatModemFormat(self):
		pass

