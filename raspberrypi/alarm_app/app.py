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

	### Changing it up a bit to use the 'with' statement to automatically close down the worker threads on 
	### the event that an exception occurs

	def __enter__(self):
		# now start the worker thread
		self.start()

		# and while that's going look for user input
		self.handleInput()
			
	def __exit__(self, type, value, tb):
		self.ShouldRun = False

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

	
	def getWakeTimeFromUser(self):
		print "Hour: "
		InputHour = raw_input()
		print "Minute: " 
		InputMin = raw_input()
		self.setWakeTime(_Hour=InputHour, _Minute=InputMin)

	def getSleepTimeFromUser(self):
		print "Hour: "
		InputHour = int(raw_input())
		print "Minute: " 
		InputMin = int(raw_input())
		self.setSleepTime(_Hour=InputHour, _Minute=InputMin)

	def handleInput(self):	
		while self.ShouldRun:
			self.UserMsg = raw_input()
			if self.UserMsg == "shutdown":
				print "shutting system down"
				self.ShouldRun = False
			elif self.UserMsg == "status":
				print "Current Status: " + self.Status
			elif self.UserMsg == "waketime":
				print "Current WakeTime: " + str(self.SetWakeTime)
			elif self.UserMsg == "set waketime":
				self.getWakeTimeFromUser()
			elif self.UserMsg == "sleeptime":
				print "Current SleepTime: " + str(self.SetSleepTime)
			elif self.UserMsg == "set sleeptime":
				self.getSleepTimeFromUser()
			else:
				print "options are:"
				print "'status' - shows whether or not the fan is on or off"
				print "'shutdown' - turn off the app"
				print "'waketime' - show the current waketime"
				print "'set waketime' - change the minute and hour of the waketime"
				print "'sleeptime' - show the current sleeptime"
				print "'set sleeptime' - change the minute and hour of the sleeptime"


if __name__ == '__main__':
	Timeout = 60
	with App(_Timeout=Timeout) as app:
		print 'System stopped, waiting for thread to exit, timeout: ' + str(Timeout)
