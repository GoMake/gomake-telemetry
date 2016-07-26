import logging
import json
import sqlite3 as sqlite
import os, sys
import sentence

class Database():
	def __init__(self, dbPath, logger=None):
		self.dbPath = dbPath
		self.connect()
		self.setupTables()
	def connect(self):
		try:
			self.conn = sqlite.connect(self.dbPath)
		except sqlite.Error, e:
			logging.error('Could not connect to database ' + dbPath)
	def dropTables(self):
		if(self.conn):
			try:
				cursor = self.conn.cursor()
				cursor.executescript("""
					DROP TABLE IF EXISTS flightdata;
					DROP TABLE IF EXISTS config;
				""")
				self.conn.commit()
			except sqlite.Error, e:
				self.conn.rollback()
				logging.error('Could not drop table in database')	
	def setupTables(self):
		if(self.conn):
			try:
				cursor = self.conn.cursor()
				cursor.executescript("""
					CREATE TABLE IF NOT EXISTS flightdata(id INTEGER PRIMARY KEY, timestamp TEXT, lat TEXT, long TEXT, alt TEXT, sensors TEXT);
				""")
				self.conn.commit()
			except sqlite.Error, e:
				self.conn.rollback()
				logging.error('Could not create table in database')
				print e
	def saveFlightRecord(self, record):
		try:
			cursor = self.conn.cursor()
			columns = ', '.join(record.keys())
			placeholders = ':'+', :'.join(record.keys())
			query = 'INSERT INTO flightdata (%s) VALUES (%s)' % (columns, placeholders)
			cursor.execute(query, record)
			self.conn.commit()
		except sqlite.Error, e:
			self.conn.rollback()
			logging.error('Could not insert record in database: ' + json.dumps(record))

if __name__ == "__main__":
	d = Database('/opt/telemetry-data/data.db')
	print d.getConfigValueByKeyName('datalogging')
	#d.dropTables()
	#d.setupTables()
	#t = {'timestamp':'2016-07-23 12:25:00','lat':'45','long':'122','alt':'2000','sensors':'apples,oranges,tomatoes'}
	#d.saveFlightRecord(t)
