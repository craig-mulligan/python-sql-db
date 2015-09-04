from db_setup import Reading, session
import time
import psutil

def log():
	cpu = psutil.cpu_percent()
	now = time.strftime('%Y-%m-%d %H:%M:%S')
	newLog = Reading(reading=cpu, timestamp=now)	
	session.add(newLog)
	session.commit()

if __name__ == '__main__':
    log()
    time.sleep(30)