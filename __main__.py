import sys, os, time, logging
from telemetry import gps
from telemetry import temperature
from telemetry import sound
from telemetry import gas
from telemetry import button
from telemetry import flightrecorder
from telemetry import flightrecord
from telemetry import lcd

dbPath = os.environ.get('DB_PATH') or 'data.db'
logPath = os.environ.get('LOG_PATH') or 'event.log'
gpsPath = os.environ.get('GPS_PATH') or '/dev/ttyS0'
gpsBaud = os.environ.get('GPS_BAUD') or 4800
satPath = os.environ.get('SAT_PATH')
satBaud = os.environ.get('SAT_BAUD')
tempSensorPin = 0
soundSensorPin = 1
gasSensorPin = 2
soundSensorPin = ''
pushButtonPin = 3

class Main():
    dataLoggingEnabled = False
    def getLCD(self):
        self.logMessage("Loading: LCD Screen...")
        return lcd.LCD()
    def getDatabase(self):
        self.logMessage("Loading: SQLite Database...")
        return flightrecorder.Database(dbPath)
    def getSatModem(self):
        self.logMessage("Loading: Satellite Modem...")
    def getGPS(self):
        self.logMessage("Loading: GPS Module...")
        return gps.GPS(gpsPath, gpsBaud, self.logger)
    def getSensors(self):
        self.logMessage("Loading: GrovePi Sensor Configuration...")
        sensors = []
        self.logMessage("Loading: LM35 Temperature Sensor...")
        tempSensor = temperature.Temperature(tempSensorPin, self.logger)
        sensors.append(tempSensor)
        #self.logMessage("Loading: Sound Sensor...")
        #soundSensor = sound.Sound(soundSensorPin, self.logger)
        #sensors.append(soundSensor)
        #self.logMessage("Loading: Gas Sensor...")
        #gasSensor = gas.Gas(gasSensorPin, self.logger)
        #sensors.append(gasSensor)
        return sensors
    def getButton(self):
        return button.Button(pushButtonPin, self.logger)
    def loadModules(self):
        self.database = self.getDatabase()
        self.satModem = self.getSatModem()
        self.gps = self.getGPS()
        self.sensorList = self.getSensors()
        self.dataLoggingButton = self.getButton()
        self.lcd = self.getLCD()
    def getCurrentTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    def logMessage(self, message):
        if(self.logger and message):
            logging.info(message)
    def setupLogging(self):
        logging.basicConfig(filename=logPath, format='%(asctime)s gomake:: %(message)s', level=logging.INFO)
        self.logger = logging.getLogger()
    def isDataLoggingEnabled(self):
        if(not self.dataLoggingEnabled):
            if(self.dataLoggingButton.read() == '1'):
		self.dataLoggingEnabled = True
		self.setLCDStatus()
        return self.dataLoggingEnabled or None
    def readSensorValues(self):
        sensorValues = {}
        for sensor in self.sensorList:
            sensorType = sensor.getType()
            sensorValue = sensor.read()
            sensorValues[sensorType] = sensorValue
            time.sleep(0.5)
        return sensorValues
    def setLCDStatus(self):
        recStatus = 'Y' if self.dataLoggingEnabled else 'N'
        statusString = 'RUN: Y' + ' REC: ' + recStatus
        if(self.lcd):
            self.lcd.setStatus(statusString)
    def run(self):
        self.logMessage('Beginning run loop...')
	self.setLCDStatus()
        while True:
            try:
                timestamp = self.getCurrentTime()
                coordinates = self.gps.read()
                #Read Sensor values
                sensorValues = self.readSensorValues()
                record = flightrecord.FlightRecord(timestamp, coordinates, sensorValues)
                #Log in log
                self.logMessage(record.getLogFormat())
                if(self.isDataLoggingEnabled()):
                    self.logMessage('Writing to database...')
                    #Record in Database
                    self.database.saveFlightRecord(record.getDatabaseFormat())
                    #Send Satellite Message
            except Exception as e:
                logging.exception(e)
    def __init__(self):
        self.setupLogging()
        self.loadModules()

if __name__ == '__main__':
    telemetry = Main()
    telemetry.run()

