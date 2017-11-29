from time_manager import TimeManager
from sched import scheduler
import time

# 30 second timeout by default

class App(TimeManager):
	def __init__(self, _Timeout = 30, _WakeHour = 1, _WakeMinute = 1):
		TimeManager.__init__(self)
		self.ShouldRun = True
		self.setTime(_Hour = _WakeHour, _Minute = _WakeMinute)
		self.Timeout = _Timeout
		self.AppScheduler = scheduler(time.time, time.sleep)
		self.setupEvent()

	def routine(self):
		self.getCurrentTime()
		print self.shouldWakeUp()

		# reset for the next round
		if self.ShouldRun:
			self.setupEvent()
	
	def setupEvent(self):
		self.AppScheduler.enter(self.Timeout, 1, self.routine, ())
		self.AppScheduler.run()
		

if __name__ == '__main__':
	app = App(_Timeout=1)
