from time_manager import TimeManager
from arduino_link import ArduinoLink
from sched import scheduler
import time

# 30 second timeout by default

class App(TimeManager):
	def __init__(self, _Timeout = 60, _WakeHour = 7, _WakeMinute = 0, _SleepHour = 23, _SleepMinute = 00):
		TimeManager.__init__(self)
		self.ShouldRun = True
		self.Link = ArduinoLink()
		self.setWakeTime(_Hour = _WakeHour, _Minute = _WakeMinute)
		self.setSleepTime(_Hour = _SleepHour, _Minute = _SleepMinute)
		self.Timeout = _Timeout
		self.AppScheduler = scheduler(time.time, time.sleep)
		self.setupEvent()

	def routine(self):
		self.getCurrentTime()
		if self.shouldWakeUp():
			print 'off'
			self.Link.turnOff()
		else:
			print 'on'
			self.Link.turnOn()

		# reset for the next round
		if self.ShouldRun:
			self.setupEvent()
	
	def setupEvent(self):
		self.AppScheduler.enter(self.Timeout, 1, self.routine, ())
		self.AppScheduler.run()
		

if __name__ == '__main__':
	app = App(_Timeout=1)
