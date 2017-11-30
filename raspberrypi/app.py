from time_manager import TimeManager
from arduino_link import ArduinoLink
from threading import Thread
from time import sleep

# 30 second timeout by default

class App(TimeManager, Thread):
	def __init__(self, _Timeout = 60, _WakeHour = 6, _WakeMinute = 30, _SleepHour = 23, _SleepMinute = 59):
		# first run base class constructors
		TimeManager.__init__(self)
		Thread.__init__(self)
		
		# next setup all components of the system	
		self.ShouldRun = True
		self.Link = ArduinoLink()
		self.setWakeTime(_Hour = _WakeHour, _Minute = _WakeMinute)
		self.setSleepTime(_Hour = _SleepHour, _Minute = _SleepMinute)
		self.Timeout = _Timeout
		
		# these members handle monitoring related tasks
		self.Status = "constructor"

		# now start the worker thread
		self.start()

		# and while that's going look for user input
		self.handleInput()

	def run(self):
		while self.ShouldRun:
			sleep(self.Timeout)
			self.getCurrentTime()
			if self.shouldWakeUp():
				self.Status = "off"
				self.Link.turnOff()
			else:
				self.Status = "on"
				self.Link.turnOn()

	def handleInput(self):	
		while self.ShouldRun:
			self.UserMsg = raw_input()
			if self.UserMsg == "shutdown":
				print "shutting system down"
				self.ShouldRun = False
			elif self.UserMsg == "status":
				print "Current Status: " + self.Status
			else:
				print "options are:\n'status' - shows whether or not the fan is on or off\n'shutdown' - turn off the app"


if __name__ == '__main__':
	app = App(_Timeout=1)
