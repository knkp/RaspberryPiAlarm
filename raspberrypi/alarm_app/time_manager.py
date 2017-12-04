from datetime import datetime, timedelta
from pytz import timezone
import pytz

class TimeManager(object):
	def __init__(self, _TZ='US/Eastern'):
		self.ThisZone = timezone(_TZ)
		self.Today = 1
	
	def getCurrentTime(self):
		self.TimeNow = self.returnLocalTime()
		self.updateDay()

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

	def updateDay(self):
		if self.Today != self.TimeNow.day:
			self.SetWakeTime.replace(day = self.TimeNow.day)
			self.SetSleepTime.replace(day = self.TimeNow.day)

	def shouldWakeUp(self):
		try:
			if self.TimeNow < self.SetWakeTime:
				return False

			elif self.TimeNow > self.SetWakeTime:
				if self.TimeNow < self.SetSleepTime:
					return True
				else:
					return False

		except AttributeError:
			return -1

if __name__ == "__main__":
	TM = TimeManager()
	TM.getCurrentTime()
	TM.setWakeTime()
	TM.setSleepTime()
	print TM.shouldWakeUp()
