# sqlalchemy-challenge
Section 10 HW

# Repository Contents

## Code
  - Contains the jupyter notebook for Step 1.
  - Contains the app.py for Step 2.
  
## Images
  - Contains the images of the graphs created in Step 1

## Resources
  - Contains the sqlite file along with the csv files used in this project.

## ReadMe
  - You're reading it now.
  

# Step 1 - Climate Analysis and Exploration
To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Use the provided [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to complete your climate analysis and data exploration.

* Use SQLAlchemy `create_engine` to connect to your sqlite database.

* Use SQLAlchemy `automap_base()` to reflect your tables into classes and save a reference to those classes called `Station` and `Measurement`.

## Precipation Analysis
* Design a query to retrieve the `date` and `prcp` values from the last 12 months of precipitation data (from the most recent date in the database).
  * There are more than one `prcp` value for each date. Calculate the average of these values so you have a single `prcp` value per date.

* Load the query results into a Pandas DataFrame and set the index to the date column.

* Sort the DataFrame values by `date`.

* Plot the results using the DataFrame `plot` method. Your plot may look different from the one below.

* Use Pandas to print the summary statistics for the precipitation data.

## Station Analysis
* Design a query to calculate the total number of stations.

* Design a query that lists all stations with their corresponding observation count in descending order.

  * Which station is the most active (i.e., has the greatest number of observations)?

* Design a query to retrieve the last 12 months of temperature observation data (TOBS) for the most active station.

  * Plot the results as a histogram with `bins=12`.


# Step 2 - Climate App
After initial analysis, create a Flask API  that is based off the queries in Step 1
### Routes

* `/`

  * Home page.

  * List all routes that are available.

* `/api/v1.0/precipitation`

  * Using the query from part 1 (most recent 12 months of precipitation data), convert the query results to a dictionary using `date` as the key and `prcp` as the value.
  * Return the JSON representation of your dictionary (note the specific format of your dictionary as required from above).

* `/api/v1.0/stations`

  * Return a JSON list of stations from the dataset.

* `/api/v1.0/tobs`
  * Query the dates and temperature observations of the **most active station** for the latest year of data.
  
  * Return a JSON list of temperature observations (TOBS) for that year.

* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`

  * Create a query that returns the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    * Hint: You will need to use a function such as `func.min`, `func.max`, `func.avg`, and `func.count` in your queries.

  * When given the start date only, calculate min, max, and avg for all dates greater than and equal to the start date.

  * When given the start and the end date, calculate the min, avg, and max for dates between the start and end date inclusive.
  
  * Return a JSONified dictionary of min, max, and avg temperatures.
