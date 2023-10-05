import os
import requests
import pymysql

def lambda_handler(event, context):
    # Fetch weather data from the API
    city_name = 'New York'  # Replace with the city you want to fetch data for
    api_key = '8d9c198bc9e93ad8123dc2b2b65743f7'  # Replace with your OpenWeather API key
    weather_api_url = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city_name}"

    response = requests.get(weather_api_url)

    if response.status_code == 200:
        weather_data = response.json()
        # Process and extract relevant data
        processed_data = process_weather_data(weather_data)

        # Connect to the RDS database
        rds_host = 'database-1.c2eufdbbl7i4.ap-south-1.rds.amazonaws.com'
        rds_user = 'admin'
        rds_password = 'test12345'
        rds_database = 'project'
        
        connection = pymysql.connect(host=rds_host, user=rds_user, password=rds_password, db=rds_database)
        cursor = connection.cursor()

        # Insert processed data into the RDS database
        insert_data_into_rds(cursor, processed_data)

        # Close database connection
        cursor.close()
        connection.commit()
        connection.close()

        return {
            'statusCode': 200,
            'body': 'Data inserted into RDS successfully.'
        }
    else:
        return {
            'statusCode': response.status_code,
            'body': 'Error fetching data from the Weather API.'
        }

def process_weather_data(data):
    # Implement data processing logic here
    # Extract and format relevant information
    processed_data = []

    if 'main' in data:
        city_name = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        weather_condition = data['weather'][0]['main']
        feels_like = data['main']['feels_like']
        wind_speed = data['wind']['speed']

        processed_data.append({
            'city_name': city_name,
            'temperature': temperature,
            'humidity': humidity,
            'weather_condition': weather_condition,
            'feels_like': feels_like,
            'wind_speed': wind_speed,
        })

    return processed_data

def insert_data_into_rds(cursor, data):
    # Implement RDS data insertion logic here
    # Loop through the data and insert it into the database
    for city_data in data:
        query = """
        INSERT INTO weather_data 
        (city, temperature, humidity, weather_condition, feels_like, wind_speed) 
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (
            city_data['city_name'],
            city_data['temperature'],
            city_data['humidity'],
            city_data['weather_condition'],
            city_data['feels_like'],
            city_data['wind_speed'],
        ))
        
#Add code to draw more conclusions
