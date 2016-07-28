import logging
import rockBlock
from rockBlock import rockBlockProtocol

class SatModem (rockBlockProtocol):
	devPath="/dev/tty.usbserial-FT0DJGSK"
	def __init__(self, satPath, logger=None):
		self.devPath = satPath
		self.modem = rockBlock.rockBlock(self.devPath, self)
	def sendMessage(self, message):
		self.modem.sendMessage(message)
	def rockBlockTxStarted(self):
		logging.info("Satellite connection established...")   
	def rockBlockTxFailed(self):
        logging.info("Satellite transmission failed...")
	def rockBlockTxSuccess(self,messageNumber):
		logging.info("Satellite transmission succeeded for message " + str(messageNumber))

if __name__ == '__main__':
	s = SatModem()

