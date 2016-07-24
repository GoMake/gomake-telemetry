import time

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
	def __init__(self, fixDataArray):
		self.setFixData(fixDataArray)
		self.checkCRC(fixDataArray)
	def setFixData(self, data):
		self.type = data[0] or ''
		self.timestamp = data[1] or str(int(time.time()))
		self.latitude = data[2] or 0
		self.latitude_direction = data[3] or ''
		self.longitude = data[4] or 0
		self.longitude_direction = data[5] or ''
		self.fix_quality = data[6] or 0
		self.satellites = data[7] or 0
		self.dilution = data[8] or 0
		self.altitude = data[9] or 0
        def isValid(self):
                return True
	def checkCRC(self, data):
		pass
