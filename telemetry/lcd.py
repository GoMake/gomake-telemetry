from grove_rgb_lcd import *

class LCD():
	def __init__(self, logger=None):
		setText("")
		setRGB(0,0,0)
	def setStatus(self, message):
		setText(message)