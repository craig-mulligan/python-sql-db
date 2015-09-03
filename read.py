from db_setup import Reading
import datetime
import psutil

def log():
	cpu = psutil.cpu_percent()
	ts = datetime.datetime()
	newLog = Item(reading=cpu, timestamp=ts)	
	session.add(newLog)
	session.commit()

if __name__ == '__main__':
    log()
    time.sleep(30)