import sys, os, time, logging
from telemetry import gps
from telemetry import temperature
from telemetry import sound
from telemetry import gas

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
pushButtonPin = ''
lcdPin = ''

class Main():
    def getDatabase(self):
        self.logMessage("Loading: SQLite Database...")
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
    def loadModules(self):
        self.database = self.getDatabase()
        self.satModem = self.getSatModem()
        self.gps = self.getGPS()
        self.sensorList = self.getSensors()
    def getCurrentTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    def logMessage(self, message):
        if(self.logger and message):
            logging.info(message)
    def setupLogging(self):
        logging.basicConfig(filename=logPath, format='%(asctime)s - gomake:: %(message)s', level=logging.INFO)
        self.logger = logging.getLogger()
    def run(self):
        self.logMessage('Beginning run loop...')
        while True:
            try:
                timestamp = self.getCurrentTime()
                coordinates = self.gps.read()
                #Read Sensor values
                sensorValues = {}
                for sensor in self.sensorList:
                    sensorType = sensor.getType()
                    sensorValue = sensor.read()
                    sensorValues[sensorType] = sensorValue
                    time.sleep(1)
                #Log in log
                #Record in Database
                #Send Satellite Message
            except Exception as e:
                logging.exception(e)
    def __init__(self):
        self.setupLogging()
        self.loadModules()

if __name__ == '__main__':
    telemetry = Main()
    telemetry.run()

