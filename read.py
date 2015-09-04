from db_setup import Reading, session
import time
import psutil

def log():
	cpu = psutil.cpu_percent()
	newLog = Reading(reading=cpu)
	session.add(newLog)
	session.commit()
	print "new log!"
	readings = session.query(Reading).all()
	for r in readings:
		print "CPU: " + str(r.reading) + "stamp: " + str(r.stamp)

if __name__ == '__main__':
    log()
    time.sleep(30)