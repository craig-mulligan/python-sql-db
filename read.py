from db_setup import Reading
import time
import psutil

def log():
	cpu = psutil.cpu_percent()
	ts = time.time()
	newLog = Item(reading=cpu, timestamp=ts)	
	session.add(newLog)
	session.commit()

if __name__ == '__main__':
    log()
    time.sleep(30)