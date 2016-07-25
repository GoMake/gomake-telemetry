import time
from grove_rgb_lcd import *

class LCD():
	def __init__(self, logger=None):
		setText("")
		setRGB(0,0,0)
	def setStatus(self, message):
		setText(message)
	def flashColor(self):
		setRGB(0,128,64)
		time.sleep(3)
		setRGB(0,0,0)
