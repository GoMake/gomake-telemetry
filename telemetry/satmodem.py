import sys, time, logging
import rockBlock
from rockBlock import rockBlockProtocol
import gps, flightrecord

def print_out_waiting(conn, msg): 
	buffer_size = str(conn.outWaiting())
	logging.info(msg + buffer_size)
	
class SatModem (rockBlockProtocol):
	devPath="/dev/tty.usbserial-FT0DJGSK"
	def __init__(self, satPath, logger=None):
		logPath = '/opt/telemetry-data/event.log'
		self.logger = logging.basicConfig(filename=logPath, format='%(asctime)s gomake:: %(message)s', level=logging.INFO)
		self.devPath = satPath
		self.modem = None
		self.connect()
	def connect(self):
		logging.info("Attempting to connect to satellite")
		try:
			print self.devPath
			self.modem = rockBlock.rockBlock(self.devPath, self)
			print_out_waiting(self.modem.s,'connect():AFTER DEFAULT CONNECT:')
			dir(self.modem)
		except Exception as e:
			logging.info('Satellite failed to initialize: {}'.format(e))
	def sendMessage(self, message):
		if(self.modem):
			print_out_waiting(self.modem.s,'sendMessage():BEFORE SENDMESSAGE:')
			self.modem.sendMessage(message)
		else:
			self.connect()
			print_out_waiting(self.modem.s,'sendMessage()->connect():AFTER CONNECT:')
	def rockBlockTxStarted(self):
		logging.info("Establishing satellite connection...")   
	def rockBlockTxFailed(self):
		print_out_waiting(self.modem.s,'rockBlockTxFailed():BEFORE FLUSH:')
		logging.info("Satellite transmission failed...")
		self.modem.s.flushOutput()
		print_out_waiting(self.modem.s,'rockBlockTxFailed():AFTER FLUSH:')
	def rockBlockTxSuccess(self,messageNumber):
		logging.info("Satellite transmission succeeded for message " + str(messageNumber))
		print_out_waiting(self.modem.s, 'rockBlockTxSuccess():AFTER TX SUCCEED EVENT:')
		
if __name__ == '__main__':
	messageString = sys.argv[1]
	s = SatModem('/dev/ttyUSB0')
	#g = gps.GPS('/dev/ttyAMA0', 4800, s.logger)
	#coordinates = g.read()
	#print str(coordinates.latitude) + ', ' + str(coordinates.longitude)
	#timestamp =time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	#record = flightrecord.FlightRecord(timestamp, coordinates, {"Sound": "368", "Gas": "0.4717", "Barometer": "1010.39", "Temperature": "30.20"})
	#s.sendMessage(record.getSatModemFormat())
	s.sendMessage(messageString)
	print 'Sent message'

