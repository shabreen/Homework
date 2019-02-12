#Creating Flask API for Climate Data
#import dependencies
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#create engine to connect with sqlite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#use automap to load orm automatically
Base = automap_base()

#reflect the tables
Base.prepare(engine, reflect=True)


Measurement = Base.classes.measurement
Station = Base.classes.station

#initiate session
session = Session(engine)

#initiate Flask
app = Flask(__name__)

#create Flask Routes
@app.route("/")
def Homepage():
    return (
        f"Welcome to the Climate App Info Page!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

#create a query for precipitation data
@app.route("/api/v1.0/precipitation")
def Precipitation():
    session = Session(engine)
    prcp_results = session.query(Measurement).all()

    # Create a dictionary and append list with precipitation data
    precipitation_data = []
    for precipitation in prcp_results:
        precipitation_dict = {}
        precipitation_dict[precipitation.date] = precipitation.prcp
        precipitation_data.append(precipitation_dict)

    return jsonify(precipitation_data)

#create a query for stations
@app.route("/api/v1.0/stations")
def Stations():
    session = Session(engine)
    station_results = session.query(Station.station).all()
    stations_list = []
    for result in station_results:
        stations_list.append(result)
    return jsonify(stations_list)

#query for the dates and temperature observations from a year from the last data point.
@app.route("/api/v1.0/tobs")
def Tobs():
    session = Session(engine)
    temp_results = session.query(Measurement.tobs).\
    filter(Measurement.date >= "2016-08-23").all()
    temp_list = []
    for result in temp_results:
        temp_list.append(result.tobs)
    return jsonify(temp_list)

#dates in the %Y-%m-%d format
@app.route("/api/v1.0/<start>")
def Start_Date_Temps(start=None):
    session = Session(engine)
    start_results = session.query(func.min(Measurement.tobs),\
                                  func.avg(Measurement.tobs),\
                                  func.max(Measurement.tobs)).\
    filter(Measurement.date >= start).all()
    start_stats = list(np.ravel(start_results))
    return jsonify(start_stats)

#dates in the %Y-%m-%d format
@app.route("/api/v1.0/<start>/<end>")
def Date_Range_Temps(start=None, end=None):
    session = Session(engine)
    s_e_results = session.query(func.min(Measurement.tobs),\
                                func.avg(Measurement.tobs),\
                                func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    s_e_temp_stats = list(np.ravel(s_e_results))
    return jsonify(s_e_temp_stats)

#define main behavior
if __name__ == '__main__':
    app.run(debug=True)