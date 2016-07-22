import sys, os, time, logging

dbPath = os.environ.get('DB_PATH') or 'data.db'
logPath = os.environ.get('LOG_PATH') or 'event.log'
gpsPath = os.environ.get('GPS_PATH')
gpsBaud = os.environ.get('GPS_BAUD')
satPath = os.environ.get('SAT_PATH')
satBaud = os.environ.get('SAT_BAUD')
tempSensorPin = ''
gasSensorPin = ''
soundSensorPin = ''
pushButtonPin = ''
lcdPin = ''

class Main():
    def getDatabase(self):
        self.logMessage("Loading: SQLite Database...")
    def getSatModem(self):
        self.logMessage("Loading: Satellite Modem...")
    def getGPS(self):
        self.logMessage("Loading: GPS Module...")
    def getSensors(self):
        self.logMessage("Loading: GrovePi Sensor Configuration...")
    def loadModules(self):
        self.database = self.getDatabase()
        self.satModem = self.getSatModem()
        self.gps = self.getGPS()
        self.sensorList = self.getSensors()
    def getCurrentTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    def logMessage(message):
        if(self.logger and message):
            self.logger.info(message)
    def setupLogging():
        self.logger = logging.basicConfig(filename=logPath, format='%(asctime)s - %(name)s:: %(message)s', level=logging.INFO)
    def run(self):
        try:
            while True:
                #Get Timestamp
                timestamp = self.getCurrentTime()
                #Read GPS value
                coordinates = self.gps.read()
                #Read Sensor values
                sensorValues = {}
                for sensor in self.sensorList:
                    sensorType = sensor.getType()
                    sensorValue = sensor.read()
                    sensorValues[sensorType] = sensorValue
                #Send Satellite Message

                time.sleep(2)
        except Exception as e:
            logging.exception(e)
            sys.exit(0)
    def __init__(self):
        self.setupLogging()
        self.loadModules()

if __name__ == '__main__':
    telemetry = Main()
    telemetry.run()

