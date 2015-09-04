rm -f -r /data/sensor.db
cd /app && python db_setup.py && python read.py