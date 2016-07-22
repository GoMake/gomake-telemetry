#!/usr/bin/env python
import serial
import signal
import sys
import time
from sensor import Sensor

class GPS(Sensor):
    name = 'GPS'
    conn = None
    lastTryTime = None
    numberOfTries = 0
    def __init__(self, serialPath, serialBaud, logger=None):
        Sensor.__init__(self, self.name, logger)
        self.serialPath = serialPath
        self.serialBaud = serialBaud
        self.connect()
    def connect(self):
        self.lastTryTime = int(time.time())
        try:
            self.conn = serial.Serial(self.serialPath,  self.serialBaud)
            self.numberOfTries = 0
        except OSError:
            self.logMessage('Failed to open serial port for GPS')
    def tryReconnect(self):
        currentTime = int(time.time())
        self.numberOfTries += 1
        if(currentTime - self.lastTryTime >= 120):
            self.connect()
    def read(self):
        if(not self.conn):
            self.tryReconnect()
        while True and self.conn:
            line = self.readLine()
            if line[:6] == '$GPGGA':
                break
            time.sleep(0.1)
    def readLine(self):
        try:
            signal.signal(signal.SIGALRM, self.handleReadError)
            signal.alarm(2)
            line = self.conn.readline()
            signal.alarm(0)
            return line
        except serial.serialutil.SerialException:
            self.logMessage('Failed to read from serial port')
        return ''
    def handleReadError(self, signum, frame):
        pass
if __name__ == "__main__":
    gps=GPS('/dev/ttyS0', 4800)
    gps.read()