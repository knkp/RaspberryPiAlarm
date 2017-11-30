from serial import Serial, SerialException
from time import sleep

class ArduinoLink(object):
	def __init__(self, _Port='/dev/ttyUSB0', _Baud = 15200):
		self.Connected = False
		try:
			self.ArduinoSer = Serial(_Port, _Baud)
			self.Connected = True
		except SerialException:
			print 'couldn\'t make a connection'
		
	def turnOn(self):
		if self.Connected:
			self.ArduinoSer.write('a')

	def turnOff(self):
		if self.Connected:
			self.ArduinoSer.write('b')

if __name__ == "__main__":
	link = ArduinoLink()
	while True:
		link.turnOn()
		sleep(5)
		link.turnOff()
		sleep(5)	
