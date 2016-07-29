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
		return flightRecord
	def getLogFormat(self):
		logStringArray = []
		logStringArray.append(str(self.coordinates.latitude))
		logStringArray.append(str(self.coordinates.longitude))
		logStringArray.append(str(self.coordinates.altitude))
		logStringArray.append(json.dumps(self.sensorValues))
		return ','.join(logStringArray)
		
	def getSatModemFormat(self):
		satModemData = []
		satModemData.append("latitude=" + str(self.coordinates.latitude))
		satModemData.append("longitude=" + str(self.coordinates.longitude))
		satModemData.append("altitude=" + str(self.coordinates.altitude))
		satmodemData.append("satellites=" + str(self.coordinates.satellites))
		satModemData.append("fix_quality=" + str(self.coordinates.fix_quality))
		for key, val in self.sensorValues.iteritems():
			satModemData.append(key + "=" + val)
		return '&'.join(satModemData)


