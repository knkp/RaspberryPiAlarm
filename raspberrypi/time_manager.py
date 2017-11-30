from datetime import datetime, timedelta
from pytz import timezone
import pytz

class TimeManager(object):
	def __init__(self, _TZ='US/Eastern'):
		self.ThisZone = timezone(_TZ)
	
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
