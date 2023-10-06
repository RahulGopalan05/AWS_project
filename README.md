# AWS_project
AWS final project 2023(weather)

## Important Note
To ensure the proper functionality of the Weather Dashboard, it is crucial to use the specified AWS services for each component. Here's a list of AWS services and resources that must be utilized:

- **Frontend Hosting**: React.js frontend should be hosted on an Amazon EC2 instance.

- **Backend Hosting**: Flask (Python) backend should also be hosted on a separate Amazon EC2 instance.

- **Database**: Weather data should be stored in an Amazon RDS database (MySQL).

- **Image and Icon Storage**: All images and weather icons should be stored in an Amazon S3 bucket.

- **Data Retrieval**: Weather data is fetched from the OpenWeather API.

- **Data Update Scheduler**: AWS CloudWatch and AWS Lambda are used to schedule periodic data updates every 15 minutes.

- **Load Balancing**: Application load balancing is achieved using Amazon Elastic Load Balancer (ELB).

Make sure to configure these services and resources correctly to enjoy the full functionality of the Weather Dashboard.


```markdown
# Weather Dashboard

## Overview
The Weather Dashboard is a web application that provides real-time weather information for various cities. It offers users the ability to check weather conditions, temperatures, humidity, and more. This README provides an overview of the project, its architecture, and how to set it up.

![Weather Dashboard Screenshot](![image](https://github.com/Hazelnut05/AWS_project/assets/74465100/69398029-c381-49ca-ba02-1577f3555637)
)

## Features
- Real-time weather data: Get the latest weather information for any city.
- Top cities: Quickly access weather data for top cities.
- User-friendly interface: Intuitive design for easy navigation.
- Weather icons: Visual representations of weather conditions.
- Detailed weather data: Includes temperature, humidity, wind speed, and more.
- Automatic data updates: Continuous weather data updates every 15 minutes.
- Load balancing: Improved application availability and performance with an Elastic Load Balancer.
- Data storage: Weather data stored in an RDS database.

## Architecture
The Weather Dashboard is built using the following technologies and services:
- Frontend: React.js
- Backend: Flask (Python)
- Database: Amazon RDS (MySQL)
- Server Hosting: Amazon EC2
- Image and Icon Storage: Amazon S3
- Data Retrieval: OpenWeather API
- Data Update Scheduler: AWS CloudWatch and AWS Lambda
- Load Balancing: Amazon Elastic Load Balancer (ELB)

## Setup
Follow these steps to set up the Weather Dashboard locally or on your own server:

1. Clone the repository:
   ```bash
   git clone https://github.com/Hazelnut05/AWS_project.git
   ```

2. Frontend Setup:
   - Navigate to the `weather-app-ui` directory:
     ```bash
     cd weather-app-ui
     ```
   - Install dependencies:
     ```bash
     npm install
     ```
   - Start the frontend app:
     ```bash
     npm start
     ```

3. Backend Setup:
   - Navigate to the `weather-app-backend` directory:
     ```bash
     cd weather-app-backend
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the backend server:
     ```bash
     python backend.py
     ```

4. Access the Weather Dashboard:
   - Open a web browser and go to `http://localhost:3000` to access the Weather Dashboard.

## Usage
- Search for a city or select one of the top cities to view weather data.
- Explore weather conditions, temperatures, humidity, and more.
- The dashboard automatically updates weather data every 15 minutes.

## License(not real, just for show)
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Weather data provided by the OpenWeather API and FreeWeather API.
- Icons from [Weather Icons](https://erikflowers.github.io/weather-icons/).

Feel free to contribute to this project or report issues by creating pull requests or submitting issues. Enjoy exploring the weather with the Weather Dashboard!



