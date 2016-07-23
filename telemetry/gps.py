#!/usr/bin/env python
import serial
import signal
import sys
import time
import logging
from sensor import Sensor
from sentence import Sentence

class GPS(Sensor):
    name = 'GPS'
    conn = None
    lastTryTime = None
    numberOfReadTries = 0
    maxNumberOfReadTries = 5
    secondsToWaitForReconnect = 120
    secondsToWaitForRead = 5
    def __init__(self, serialPath, serialBaud, logger=None):
        Sensor.__init__(self, self.name, logger)
        self.serialPath = serialPath
        self.serialBaud = serialBaud
        self.connect()
    def connect(self):
        self.lastTryTime = int(time.time())
        try:
            self.conn = serial.Serial(self.serialPath,  self.serialBaud)
            self.numberOfReadTries = 0
        except OSError:
            self.logMessage('Failed to open serial port for GPS')
    def tryReconnect(self):
        currentTime = int(time.time())
        if(currentTime - self.lastTryTime >= self.secondsToWaitForReconnect):
            self.connect()
    def read(self):
        if(not self.conn):
            self.tryReconnect()
        while self.conn:
            hasReadTriesLeft = self.numberOfReadTries < self.maxNumberOfReadTries
            if not hasReadTriesLeft:
                break
            line = self.readLine() # '$GPGGA,123519,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47'
            if line[:6] == '$GPGGA':
                sentence = self.getSentence(line)
                if(sentence.isValid()):
                    return sentence
            self.numberOfReadTries += 1
            time.sleep(0.1)
        return None
    def readLine(self):
        try:
            signal.signal(signal.SIGALRM, self.handleReadError)
            signal.alarm(self.secondsToWaitForRead)
            line = self.conn.readline()
            signal.alarm(0)
            self.numberOfReadTries = 0
            return line
        except serial.serialutil.SerialException:
            self.numberOfReadTries += 1
            self.logMessage('Failed to read from serial port')
        return ''
    def handleReadError(self, signum, frame):
        pass
    def getSentence(self, line):
        fixDataArray = line.split(',')
        return Sentence(fixDataArray)
if __name__ == "__main__":
    gps=GPS('/dev/ttyS0', 4800)
    coords = gps.read()
    print coords
    print coords.latitude
