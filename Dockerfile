FROM resin/raspberrypi2-python

RUN pip install sqlalchemy psutil

# copy current directory into /app
COPY . /app

# run python script when container lands on device
CMD ["bash", "/app/start.sh"]
