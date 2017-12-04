from flask import request

@app.route('/get_times', methods=['GET'])
def get_times():
	# pull times from the database and return it as json

@app.route('/set_wake_time', methods=['POST'])
def set_wake_time()	
	# insert the wake time into the database

@app.route('/set_sleep_time', methods=['POST'])
def set_sleep_time()	
	# insert the sleep time into the database
