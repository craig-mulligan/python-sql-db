from db_setup import Reading
import datetime
import psutil

def log():
	cpu = psutil.cpu_percent()
	ts = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	newLog = Item(reading=cpu, timestamp=ts)	
	session.add(newLog)
	session.commit()

if __name__ == '__main__':
    log()
    time.sleep(30)