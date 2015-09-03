#!/usr/bin/python
import os
import sys
from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
 
Base = declarative_base()
 
class Reading(Base):
    __tablename__ = 'reading'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    reading = Column(Integer, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    
    # This will be used when we implement an API that returns json
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'reading': self.reading,
            'timestamp': self.timestamp
        }
 
# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///../data/sensor.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)


# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()