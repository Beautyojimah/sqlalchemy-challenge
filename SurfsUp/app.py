# Import the dependencies.

import numpy as np

import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    
    return (
        "Welcome to Hawaii Weather Analysis! <p/>"
        f"Here are the available endpoints:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the start date for the last 12 months
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    start_date = (dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)).strftime("%Y-%m-%d")
    
    # Query the precipitation data for the last 12 months
    prcp_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= start_date).all()
    
    # Convert the query results to a dictionary with date as the key and prcp as the value
    prcp_dict = {date: prcp for date, prcp in prcp_data}
    
    return jsonify(prcp_dict)
   

@app.route("/api/v1.0/stations")
def stations():
     # Query all stations from the Station table
    station_data = session.query(Station.station, Station.name).all()
    
     # Convert the query results to a list of dictionaries
    station_list = [{"station": station, "name": name} for station, name in station_data]
    
    return jsonify(station_list)
    

@app.route("/api/v1.0/tobs")
def tobs():
     # Identify the most active station
    most_active_station = session.query(Measurement.station).\
                          group_by(Measurement.station).\
                          order_by(func.count(Measurement.station).desc()).\
                          first()[0]
    
    # Calculate the start date for the last 12 months
    most_recent_date = session.query(Measurement.date).\
                       filter(Measurement.station == most_active_station).\
                       order_by(Measurement.date.desc()).first()[0]
    start_date = (dt.datetime.strptime(most_recent_date, "%Y-%m-%d") - dt.timedelta(days=365)).strftime("%Y-%m-%d")
    
    # Query the temperature observations for the last 12 months for the most active station
    tobs_data = session.query(Measurement.date, Measurement.tobs).\
                filter(Measurement.station == most_active_station).\
                filter(Measurement.date >= start_date).all()
    
    # Convert the query results to a list of dictionaries
    tobs_list = [{"date": date, "tobs": tobs} for date, tobs in tobs_data]
    
    return jsonify(tobs_list)
    

@app.route("/api/v1.0/<start>")
def start_temp(start):
    
    # Query to calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date
    temp_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                 filter(Measurement.date >= start).all()
    
    # Convert the query results to a dictionary
    temp_dict = {
        "TMIN": temp_stats[0][0],
        "TAVG": temp_stats[0][1],
        "TMAX": temp_stats[0][2]
    }
    
    return jsonify(temp_dict)

@app.route("/api/v1.0/<start>/<end>")
def range_temp(start, end):
    

    temp_range_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                       filter(Measurement.date >= start).\
                       filter(Measurement.date <= end).all()
    
    # Convert the query results to a dictionary
    temp_range_dict = {
        "TMIN": temp_range_stats[0][0],
        "TAVG": temp_range_stats[0][1],
        "TMAX": temp_range_stats[0][2]
    }
    
    return jsonify(temp_range_dict)


@app.after_request
def close_session(response):
    session.close()
    return response


if __name__ == "__main__":
    app.run(debug=True)