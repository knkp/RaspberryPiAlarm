from datetime import datetime, timedelta
from pytz import timezone
import pytz

class TimeManager(object):
	def __init__(self, _TZ='US/Eastern'):
		self.ThisZone = timezone(_TZ)
		self.Today = 1
	
	def getCurrentTime(self):
		self.TimeNow = self.returnLocalTime()

	def setWakeTime(self, _Hour=12, _Minute=30):
		Time = self.returnLocalTime()
		Time = Time.replace(hour = _Hour, minute = _Minute)
		self.SetWakeTime = Time

	def setSleepTime(self, _Hour=12, _Minute=30):
		Time = self.returnLocalTime()
		Time = Time.replace(hour = _Hour, minute = _Minute)
		self.SetSleepTime = Time

	def returnLocalTime(self):
		Time = datetime.utcnow()
		UtcDT = pytz.UTC.localize(Time)
		LocDT = UtcDT.astimezone(self.ThisZone)
		return LocDT

	def shouldWakeUp(self):
		try:
			hours = False
			minutes = False

			if self.TimeNow.hour < self.SetWakeTime.hour:
				hours =  False

			elif self.TimeNow.hour > self.SetWakeTime.hour:
				if self.TimeNow.hour < self.SetSleepTime.hour:
					hours = True
				else:
					hours = False
			
			if self.TimeNow.minute < self.SetWakeTime.minute:
				minutes =  False

			elif self.TimeNow.minute > self.SetWakeTime.minute:
				if self.TimeNow.minute < self.SetSleepTime.minute:
					minutes = True
				else:
					minutes = False

			if hours:
				if minutes:
					return True

			return False

		except AttributeError:
			return -1


if __name__ == "__main__":
	TM = TimeManager()
	TM.getCurrentTime()
	TM.setWakeTime()
	TM.setSleepTime()
	print TM.shouldWakeUp()
