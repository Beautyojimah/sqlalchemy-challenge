# Sqlalchemy-challenge involving Climate Analysis and Exploration with Flask API

This project provides a climate analysis of Honolulu, Hawaii, and serves the results via a Flask API. The data is sourced from SQLite databases and the analysis is performed using SQLAlchemy ORM, Pandas, and Matplotlib.

The repository contains a `SurfsUp` folder. Within this folder is the jupyter notebook (`climate_starter.ipynb`) and python file (`app.py`), which holds the codes for the climate analysis and the codes for serving the results bia flask, respectively.   

The resource folder holds the csv files used for this analysis. 

## Features

- **Precipitation Analysis**: Retrieves the last 12 months of precipitation data and plots the results.

- **Station Analysis**: Displays information about weather stations, including the most active ones and temperature statistics for them.

- **Temperature Analysis**: Offers insights into temperature patterns with a histogram.

- **Flask API Endpoints**: Allows for data retrieval for various analyses via API calls.
    - Precipitation data
    - Station information
    - Temperature observations
    - Temperature statistics for specific date ranges

## Getting Started

### Prerequisite

- Python
- SQLite
- SQLAlchemy
- Flask
- Pandas
- Numpy
- Datetime
- Matplotlib

### Installation and Setup

1. **Clone the Repository**:
Using  git clone `https://github.com/Beautyojimah/sqlalchemy-challenge.git`

2. **Navigate to Project Directory**:
Using `cd <path_to_directory>`

3. **Set Up Virtual Environment**:
Using `python -m venv .venv` to create a virtual environment
Use `.venv\Scripts\activate` to activate the virtual environment 

4. **Database Setup**:
Use the provided SQLite database file contained in the `Resources` folder. 

5. **Run the Flask Application**:
Set up FLASK_APP environment variable in the command line using `set FLASK_APP=app.py`.
To run flask use `flask run`.

## API Usage

- **Home** (`/`): A list of all available routes.

- **Precipitation Data** (`/api/v1.0/precipitation`): Returns the last 12 months of precipitation data in JSON format.

- **Stations** (`/api/v1.0/stations`): Provides a list of all stations in JSON format.

- **Temperature Observations** (`/api/v1.0/tobs`): Displays temperature observations of the most active station over the past year in JSON format.

- **Temperature Range** (`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`): Offers minimum, average, and maximum temperatures for a specified date range in JSON format.

## Technologies

- **Backend**: Python, SQLite, SQLAlchemy, Flask
- **Data Analysis**: Pandas, Matplotlib







