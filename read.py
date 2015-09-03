from db_setup import Reading, session
import time
import psutil

DBSession = sessionmaker(bind=engine)
session = DBSession()

def log():
	cpu = psutil.cpu_percent()
	ts = time.time()
	newLog = Reading(reading=cpu, timestamp=ts)	
	session.add(newLog)
	session.commit()

if __name__ == '__main__':
    log()
    time.sleep(30)