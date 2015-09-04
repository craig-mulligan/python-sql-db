from db_setup import Reading, session
import time
import psutil

def log():
	cpu = psutil.cpu_percent()
	now = time.ctime(int(time.time()))
	newLog = Reading(reading=cpu, timestamp=now)	
	session.add(newLog)
	session.commit()

if __name__ == '__main__':
    log()
    time.sleep(30)