import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_

from flask import Flask, jsonify

# Database Setup
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)

# Tables from Database
measurement_table = Base.classes.measurement
station_table = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def home():
    return(
        f"Welcome to the Home Page!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/'startdate'<br/>"
        f"/api/v1.0/'startdate'/'enddate'<br/>"
        f"Date Format is: yyyy-mm-dd"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create a Session to the database
    session = Session(engine)

    results = session.query(measurement_table.date, measurement_table.prcp).\
                filter(measurement_table.date >= (dt.date(2017, 8, 23) - dt.timedelta(weeks = 52))).\
                order_by(measurement_table.date).all()

    session.close()

    # Create a dictionary from results
    prcp_list = []
    for date, prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_list.append(prcp_dict)
    
    return jsonify(prcp_list)

@app.route("/api/v1.0/stations")
def stations():
    # Create a Session to the database
    session = Session(engine)

    # Query the station id and name in the Station table
    results = session.query(station_table.station, station_table.name).all()

    session.close()

    return jsonify(results)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create a Session to the database
    session = Session(engine)

    # Query the temps for each date, for the most active station: USC005129281
    results = session.query(measurement_table.date, measurement_table.tobs).\
                filter(measurement_table.date >= (dt.date(2017, 8, 23) - dt.timedelta(weeks = 52))).\
                filter(measurement_table.station == "USC00519281").all()

    session.close()

    return jsonify(results)

@app.route("/api/v1.0/<startDate>")
def startDate(startDate):
    # Create a Session to the database
    session = Session(engine)

    # Query the min, avg, and max temperatures for all of the dates after the 'startDate'
    results = session.query(func.min(measurement_table.tobs), \
                func.avg(measurement_table.tobs), \
                func.max(measurement_table.tobs)).\
                filter(measurement_table.date >= startDate).\
                group_by(measurement_table.date).all()

    session.close()

    return jsonify(results)

@app.route("/api/v1.0/<startDate>/<endDate>")
def endDate(startDate, endDate):
    # Create a Session to the database
    session = Session(engine)

    # Query the min, avg, and max temperatures for all of the dates between the 'startDate' and 'endDate'
    results = session.query(func.min(measurement_table.tobs), \
                func.avg(measurement_table.tobs), \
                func.max(measurement_table.tobs)).\
                filter(measurement_table.date >= startDate).\
                filter(measurement_table.date <= endDate).\
                group_by(measurement_table.date).all()

    session.close()

    return jsonify(results)

if __name__ == "__main__":
    app.run(debug = True)