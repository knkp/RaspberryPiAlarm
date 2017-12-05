import sqlite3 as lite
import sys
import os

def createDatabase():
	con = lite.connect(os.environ['PI_ALARM_DB'])
	with con:
	    cur = con.cursor()    
	    cur.execute("CREATE TABLE SleepTimes(hour INT, minute INT)")
	    cur.execute("CREATE TABLE WakeTimes(hour INT, minute INT)")

def returnTimes():
	con = lite.connect(os.environ['PI_ALARM_DB'])
	with con:
		cur = con.cursor()
		cur.execute("SELECT hour, minute FROM SleepTimes")
		rows = cur.fetchall()
		#print 'sleeptime'
		#print 'hours, minutes:'
		sleeptime =  rows[-1]
		cur.execute("SELECT hour, minute FROM WakeTimes")
		rows = cur.fetchall()
		#print 'waketime'
		#print 'hours, minutes:'
		waketime = rows[-1]
		return [waketime, sleeptime]

def updateSleepTime(hour, minute):
	con = lite.connect(os.environ['PI_ALARM_DB'])
	with con:
		cur = con.cursor()
		cur.execute('''REPLACE INTO SleepTimes(hour, minute) VALUES(?, ?)''', (hour, minute))

def updateWakeTime(hour, minute):
	con = lite.connect(os.environ['PI_ALARM_DB'])
	with con:
		cur = con.cursor()
		cur.execute('''REPLACE INTO WakeTimes(hour, minute) VALUES(?, ?)''', (hour, minute))

if __name__ == "__main__":
	print 'creating time manager database'
	createDatabase()
	print 'database created'
