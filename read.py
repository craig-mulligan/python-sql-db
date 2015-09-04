from db_setup import Reading, session
import time
import psutil

def log():
	cpu = psutil.cpu_percent()
	newLog = Reading(reading=cpu)	
	session.add(newLog)
	session.commit()

if __name__ == '__main__':
    log()
    time.sleep(30)