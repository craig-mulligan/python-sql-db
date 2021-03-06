# python imports
import psutil
import os 

# import sqlchemy refs
from db_setup import Reading, session

# read environment variables + set defaults
interval = os.getenv('INTERVAL', '20');

def log():
	cpu = psutil.cpu_percent()
	newLog = Reading(reading=cpu)
	session.add(newLog)
	session.commit()
	print "CPU: " + str(cpu)

def all_logs():
	readings = session.query(Reading).all()
	for r in readings:
		print "CPU: " + str(r.reading) + ", stamp: " + str(r.stamp)
	
while True:
    log()
    time.sleep(int(interval))
