import time, re
import pynmea2

"""
$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47

	 GGA          Global Positioning System Fix Data
	 123519       Fix taken at 12:35:19 UTC
	 4807.038,N   Latitude 48 deg 07.038' N
	 01131.000,E  Longitude 11 deg 31.000' E
	 1            Fix quality: 0 = invalid
							   1 = GPS fix (SPS)
							   2 = DGPS fix
							   3 = PPS fix
				   4 = Real Time Kinematic
				   5 = Float RTK
							   6 = estimated (dead reckoning) (2.3 feature)
				   7 = Manual input mode
				   8 = Simulation mode
	 08           Number of satellites being tracked
	 0.9          Horizontal dilution of position
	 545.4,M      Altitude, Meters, above mean sea level
	 46.9,M       Height of geoid (mean sea level) above WGS84
					  ellipsoid
	 (empty field) time in seconds since last DGPS update
	 (empty field) DGPS station ID number
	 *47          the checksum data, always begins with *

"""

class Sentence():
	def __init__(self, line):
		try:
			data = pynmea2.parse(line)
			self.setFixData(data)
		except:
			self.setEmptyData()
	def setFixData(self, data):
		self.type =  'GGA'
		self.timestamp = data.timestamp or str(int(time.time()))

		self.latitude = data.latitude or '0'
		self.latitude_direction = data.lat_dir or 'N'

		self.longitude = data.longitude or '0'
		self.longitude_direction = data.lon_dir or 'W'

		self.fix_quality = data.gps_qual or '0'
		self.satellites = data.num_sats or '0'
		self.dilution = data.horizontal_dil or '0'
		self.altitude = data.altitude or '0'
	def isValid(self):
		return True
	def setEmptyData(self):
		self.type = 'GGA'
		self.timestamp = str(int(time.time()))
		self.latitude = '0'
		self.latitude_direction = ''
		self.longitude = '0'
		self.longitude_direction = ''
		self.fix_quality = '0'
		self.satellites = '0'
		self.dilution = '0'
		self.altitude = '0'
