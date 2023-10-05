from flask import Flask, request, jsonify, redirect
import requests
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define your database connection settings here
app.config['DATABASE_SETTINGS'] = {
    'host': 'database-1.c2eufdbbl7i4.ap-south-1.rds.amazonaws.com',
    'user': 'admin',
    'password': 'test12345',
    'database': 'project'  # Specify the target database
}

# Create a function to establish a MySQL database connection
def create_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host=app.config['DATABASE_SETTINGS']['host'],
            user=app.config['DATABASE_SETTINGS']['user'],
            password=app.config['DATABASE_SETTINGS']['password'],
            database=app.config['DATABASE_SETTINGS']['database']  # Specify the target database here
        )
        return connection
    except Exception as e:
        print("Error connecting to MySQL:", str(e))
        return None

# Create a function to delete all data from the "weather_data" table
def delete_all_data():
    try:
        connection = create_mysql_connection()  # Specify the target database here
        cursor = connection.cursor()

        # Delete all data from the "weather_data" table
        delete_query = "DELETE FROM weather_data"
        cursor.execute(delete_query)

        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print("Error deleting data:", str(e))

# Call the delete_all_data function to remove previous data at the beginning of each run
delete_all_data()

# Create a function to create the "project" database (if it doesn't exist)
def create_database():
    try:
        connection = create_mysql_connection()
        cursor = connection.cursor()

        # Create the "project" database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS project")

        cursor.close()
        connection.close()
    except Exception as e:
        print("Error creating database:", str(e))

# Create a function to create the "weather_data" table (if it doesn't exist)
def create_weather_table():
    try:
        connection = create_mysql_connection()  # Specify the target database here
        cursor = connection.cursor()

        # Create the "weather_data" table if it doesn't exist with the desired column name
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                id INT AUTO_INCREMENT PRIMARY KEY,
                city VARCHAR(255) NOT NULL,
                temperature DECIMAL(5, 2) NOT NULL,
                feels_like DECIMAL(5, 2) NOT NULL,
                humidity INT NOT NULL,
                wind_speed DECIMAL(5, 2) NOT NULL,
                weather_condition VARCHAR(255) NOT NULL  # Change the column name here
            )
        """)

        cursor.close()
        connection.close()
    except Exception as e:
        print("Error creating table:", str(e))

# Call the create_database and create_weather_table functions to ensure they exist
create_database()
create_weather_table()

# Create a function to establish a MySQL database connection for the "project" database
def create_mysql_connection_project():
    try:
        connection = mysql.connector.connect(
            host=app.config['DATABASE_SETTINGS']['host'],
            database='project',  # Use the "project" database
            user=app.config['DATABASE_SETTINGS']['user'],
            password=app.config['DATABASE_SETTINGS']['password']
        )
        return connection
    except Exception as e:
        print("Error connecting to MySQL (project database):", str(e))
        return None

# Create a function to get weather data and store it in the database
@app.route('/api/get_weather', methods=['GET'])
def get_weather_data():
    city_name = request.args.get('city')
    api_key = "a50e6da50c9e45b08b834226232109"  # Replace with your WeatherAPI API key
    weather_api_url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&units=metric"

    try:
        response = requests.get(weather_api_url)
        response.raise_for_status()

        weather_data = response.json()

        if 'current' in weather_data:
            temperature = weather_data['current']['temp_c']
            feels_like = weather_data['current']['feelslike_c']
            humidity = weather_data['current']['humidity']
            wind_speed = weather_data['current']['wind_kph']
            condition = weather_data['current']['condition']['text']

            # Create a dictionary to hold the data
            data = {
                "city": city_name,
                "weather": {
                    "main": condition.capitalize(),
                    "description": condition,
                    "icon": "some_icon_code"  # You can replace this with the actual icon code
                },
                "main": {
                    "temp": temperature,
                    "feels_like": feels_like,
                    "humidity": humidity
                },
                "wind": {
                    "speed": wind_speed
                }
            }

            # Call the insert_weather_data function with the data dictionary
            insert_weather_data(data)

            # Return the weather data as JSON response
            return jsonify(data)

        else:
            return jsonify({"error": "Weather data not available."}), 404
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Error fetching weather data: {str(e)}"}), 500

# Create a function to insert weather data into the "weather_data" table
def insert_weather_data(data):
    try:
        connection = create_mysql_connection_project()  # Use the "project" database

        if connection:
            cursor = connection.cursor()

            # Insert data into the "weather_data" table with updated columns
            insert_query = "INSERT INTO weather_data (city, temperature, feels_like, humidity, wind_speed, weather_condition) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(insert_query, (data['city'], data['main']['temp'], data['main']['feels_like'], data['main']['humidity'], data['wind']['speed'], data['weather']['main']))
            connection.commit()
            cursor.close()
            connection.close()

            # Print a success message
            print("Data inserted successfully for city:", data['city'])
            return jsonify({"message": "Data inserted successfully."}), 200
        else:
            return jsonify({"error": "Database connection error."}), 500
    except Exception as e:
        # Print the error message
        print("Error inserting data into the database:", str(e))
        return jsonify({"error": "Error inserting data into the database: " + str(e)}), 500

# Define a root route to redirect to /api/get_weather
@app.route('/', methods=['GET'])
def root_redirect():
    if request.method == 'GET':
        # Redirect to /api/get_weather
        return redirect('/api/get_weather')

if __name__ == '__main__':
    app.run()
