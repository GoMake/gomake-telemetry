import logging
import sqlite3 as sqlite
import os, sys
import sentence

class Database():
	def __init__(self, dbPath, logger=None):
		try:
			sqlite.connect(dbPath)
		except sqlite.Error, e:
			logging.error('Could not connect to database ' + dbPath)
		finally:
			if self.conn:
				self.conn.close()
	def setupTables(self):
		pass
	def saveSentence(self):
		pass