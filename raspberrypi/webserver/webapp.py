from flask import request, Flask
import json

# this allows us to pull the database module from the parallel directory,
# without carrying the same risks as a relative import

import inspect
import os
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0,parentdir)

import database.dbaccess as db

app = Flask(__name__)

@app.route('/get_times', methods=['GET'])
def get_times():
	# pull times from the database and return it as json
	times = db.returnTimes()
	wakehour = times[0][0]
	wakeminute = times[0][1]
	sleephour = times[1][0]
	sleepminute = times[1][1]
	times_dict = {
		'sleeptimes':{
			'hour':wakehour,
			'minute':wakeminute
		},
		'waketimes':{
			'hour':sleephour,
			'minute':sleepminute
		}
	}
	return str(times_dict)

@app.route('/set_wake_time', methods=['POST'])
def set_wake_time():	
	# insert the wake time into the database
	pass

@app.route('/set_sleep_time', methods=['POST'])
def set_sleep_time():	
	# insert the sleep time into the database
	pass

if __name__ == '__main__':
	app.run()
