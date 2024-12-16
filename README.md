"""
Climate Analysis and Flask API

Project Overview:
This project analyzes weather data for Hawaii using Python, SQLAlchemy, and Flask. 
The data is stored in a SQLite database and includes precipitation, temperature, 
and station information. A Flask API is created to provide easy access to the 
results of the analysis.

Files:
1. hawaii.sqlite - The SQLite database containing the climate data.
2. climate_starter.ipynb - A Jupyter Notebook used to perform data exploration and visualization.
3. app.py - The Flask application that provides API routes to access the climate data.

Database Structure:
- Measurement: Contains the recorded data (precipitation, temperature observations, 
  date, and station ID).
- Station: Contains metadata about weather stations.

Flask API Routes:
1. Homepage: 
   Route: `/` 
   Description: Displays a list of available routes.

2. Precipitation Data:
   Route: `/api/v1.0/precipitation`
   Description: Returns the last 12 months of precipitation data as a JSON object.

3. Stations:
   Route: `/api/v1.0/stations`
   Description: Returns a JSON list of weather stations.

4. Temperature Observations (TOBS):
   Route: `/api/v1.0/tobs`
   Description: Returns the temperature observations for the most active station 
   for the last 12 months.

5. Temperature Statistics:
   Route: `/api/v1.0/<start>` 
   Description: Returns the minimum, average, and maximum temperatures from the 
   start date to the end of the dataset.

   Route: `/api/v1.0/<start>/<end>` 
   Description: Returns the minimum, average, and maximum temperatures for the 
   specified date range.

How to Run the Project:

Prerequisites:
Ensure the following Python libraries are installed:
- Flask
- SQLAlchemy
- Pandas
- NumPy
- Matplotlib

Install these libraries using pip:
pip install flask sqlalchemy pandas numpy matplotlib

Steps to Run:
1. Clone the repository:
   git clone <https://github.com/DWallace740/sqlalchemy-challenge.git>
   cd sqlalchemy-challenge

2. Start the Flask app:
   python app.py

3. Open your browser and visit:
   http://127.0.0.1:5000/

4. Test the following routes in your browser:
   - Homepage: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
   - Precipitation Data: [http://127.0.0.1:5000/api/v1.0/precipitation](http://127.0.0.1:5000/api/v1.0/precipitation)
   - Stations: [http://127.0.0.1:5000/api/v1.0/stations](http://127.0.0.1:5000/api/v1.0/stations)
   - Temperature Observations (TOBS): [http://127.0.0.1:5000/api/v1.0/tobs](http://127.0.0.1:5000/api/v1.0/tobs)
   - Temperature Statistics with Start Date: [http://127.0.0.1:5000/api/v1.0/2016-08-23](http://127.0.0.1:5000/api/v1.0/2016-08-23)
   - Temperature Statistics with Start/End Dates: [http://127.0.0.1:5000/api/v1.0/2016-08-23/2017-08-23](http://127.0.0.1:5000/api/v1.0/2016-08-23/2017-08-23)


Output Images:
Include these key screenshots in your project submission to demonstrate functionality:
1. Flask API Homepage - A screenshot of the homepage listing all available routes.
2. Precipitation Route - A screenshot of the JSON output from the `/api/v1.0/precipitation` route.
3. Stations Route - A screenshot of the JSON output from the `/api/v1.0/stations` route.
4. TOBS Route - A screenshot of the JSON output from the `/api/v1.0/tobs` route.
5. Visualization Outputs:
   - Precipitation bar chart from the Jupyter Notebook.
   - TOBS histogram from the Jupyter Notebook.

Resources Used:
- ChatGPT (AI Assistant): Assisted with structuring Flask routes, SQLAlchemy queries, 
  debugging code, and formatting this document.
- Xpert Learning Assistant: Used for assistance in understanding and applying concepts.
- Flask Documentation: Used for setting up routes and understanding API development.
- SQLAlchemy Documentation: Helped with ORM queries and reflecting the database.
- Matplotlib and Pandas Documentation: Used for creating visualizations and handling data.

License:
This project is licensed under the MIT License.
"""