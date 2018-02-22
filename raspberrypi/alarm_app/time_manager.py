from datetime import datetime, timedelta
from pytz import timezone
import pytz

class TimeManager(object):
	def __init__(self, _TZ='US/Eastern'):
		self.ThisZone = timezone(_TZ)
		self.Today = 1
		self.WatchTimes = False
	
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

	def floatTime(self, TimeToConv):
		Hour_flt = float(TimeToConv.hour)
		Hour_percent = float(TimeToConv.minute)/60.0
		Time_flt = Hour_flt + Hour_percent
		return Time_flt 

	def shouldWakeUp(self):
		TimeNow_flt = self.floatTime(self.TimeNow)
		SleepTime_flt = self.floatTime(self.SetSleepTime)
		WakeTime_flt = self.floatTime(self.SetWakeTime)

		if self.WatchTimes:
			print "\n"
			print 'TimeNow: ' + str(TimeNow_flt)
			print 'SleepTime: ' + str(SleepTime_flt)
			print 'WakeTime: ' + str(WakeTime_flt)
			print "\n"

		if TimeNow_flt < WakeTime_flt:
			return False
		elif TimeNow_flt > WakeTime_flt:
			if TimeNow_flt < SleepTime_flt:
				return True
			else:
				return False

if __name__ == "__main__":
	TM = TimeManager()
	TM.getCurrentTime()
	TM.setWakeTime()
	TM.setSleepTime()
	print TM.shouldWakeUp()
