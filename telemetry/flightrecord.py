import logging
import json

class FlightRecord():
	def __init__(self, timestamp, coordinates, sensorValues):
		self.timestamp = timestamp
		self.coordinates = coordinates or {}
		self.sensorValues = sensorValues
	def getDatabaseFormat(self):
		"""
		timestamp TEXT, lat TEXT, long TEXT, alt TEXT, sensors TEXT
		"""
		flightRecord = {}
		flightRecord['timestamp'] = self.timestamp or ''
		flightRecord['lat'] = self.coordinates.latitude or ''
		flightRecord['long'] = self.coordinates.longitude or ''
		flightRecord['alt'] = self.coordinates.altitude or ''
		flightRecord['sensors'] = json.dumps(self.sensorValues)

	def getLogFormat(self):
		logStringArray = []
		logStringArray.append(str(self.coordinates.latitude))
		logStringArray.append(str(self.coordinates.longitude))
		logStringArray.append(str(self.coordinates.altitude))
		logStringArray.append(json.dumps(self.sensorValues))
		return ','.join(logStringArray)
		
	def getSatModemFormat(self):
		pass

