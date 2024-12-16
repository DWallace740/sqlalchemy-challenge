# Import the dependencies
import numpy as np
import pandas as pd
from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt

#################################################
# Database Setup
#################################################

# Connect to the SQLite database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect the database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)

# Save references to the tables
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session (link) from Python to the database
session = Session(engine)

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Home route: List all available routes
@app.route("/")
def welcome():
    """List all available API routes with clickable links."""
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Hawaii Climate API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            h1 { color: #2F4F4F; }
            ul { list-style-type: none; padding: 0; }
            li { margin: 10px 0; }
            a { text-decoration: none; color: #4682B4; font-weight: bold; }
            a:hover { color: #2F4F4F; }
        </style>
    </head>
    <body>
        <h1>Welcome to the Hawaii Climate Analysis API!</h1>
        <p>Here are the available routes:</p>
        <ul>
            <li><a href="/api/v1.0/precipitation">Precipitation Data</a></li>
            <li><a href="/api/v1.0/stations">Stations</a></li>
            <li><a href="/api/v1.0/tobs">Temperature Observations (TOBS)</a></li>
            <li><a href="/api/v1.0/2016-08-23">Temperature Summary from Start Date</a></li>
            <li><a href="/api/v1.0/2016-08-23/2017-08-23">Temperature Summary for Date Range</a></li>
        </ul>
        <p><em>Note:</em> Replace the dates in the last two links with your own start or start/end dates.</p>
    </body>
    </html>
    """

# Precipitation route: JSON of date and precipitation for the last year
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return JSON of precipitation data for the last year."""
    # Find the most recent date in the dataset
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d")
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query for the last 12 months of precipitation data
    results = (
        session.query(Measurement.date, Measurement.prcp)
        .filter(Measurement.date >= one_year_ago)
        .all()
    )

    # Convert to dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)

# Stations route: JSON of all stations
@app.route("/api/v1.0/stations")
def stations():
    """Return JSON of all stations."""
    results = session.query(Station.station).all()
    stations = [station[0] for station in results]
    return jsonify(stations=stations)

# TOBS route: JSON of temperature observations for the most active station
@app.route("/api/v1.0/tobs")
def tobs():
    """Return JSON of TOBS data for the last year from the most active station."""
    # Identify the most active station
    most_active_station = (
        session.query(Measurement.station, func.count(Measurement.station))
        .group_by(Measurement.station)
        .order_by(func.count(Measurement.station).desc())
        .first()
    )[0]

    # Find the most recent date and calculate one year ago
    most_recent_date = session.query(func.max(Measurement.date)).scalar()
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d")
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query TOBS data
    results = (
        session.query(Measurement.date, Measurement.tobs)
        .filter(Measurement.date >= one_year_ago)
        .filter(Measurement.station == most_active_station)
        .all()
    )

    # Convert to list of dictionaries
    tobs_data = [{"date": date, "tobs": tobs} for date, tobs in results]

    return jsonify(tobs_data)

# Start route: JSON of TMIN, TAVG, TMAX for all dates >= start
@app.route("/api/v1.0/<start>")
def start(start):
    """Return min, avg, and max temperatures for dates >= start."""
    results = (
        session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs),
        )
        .filter(Measurement.date >= start)
        .all()
    )

    summary = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2],
    }

    return jsonify(summary)

# Start/End route: JSON of TMIN, TAVG, TMAX for a date range
@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    """Return min, avg, and max temperatures for dates between start and end."""
    results = (
        session.query(
            func.min(Measurement.tobs),
            func.avg(Measurement.tobs),
            func.max(Measurement.tobs),
        )
        .filter(Measurement.date >= start)
        .filter(Measurement.date <= end)
        .all()
    )

    summary = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2],
    }

    return jsonify(summary)


#################################################
# Debug and Run
#################################################

if __name__ == "__main__":
    app.run(debug=True)