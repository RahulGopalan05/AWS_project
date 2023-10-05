import React, { useEffect, useState } from 'react';
import { CircularProgress, Slide, TextField } from "@mui/material";
import axios from 'axios';
import "./App.css";

function App() {
  const [cityName, setCityName] = useState("Chennai"); // Default city
  const [inputText, setInputText] = useState("");
  const [data, setData] = useState({});
  const [error, setError] = useState(false);
  const [loading, setLoading] = useState(true);
  const [selectedCity, setSelectedCity] = useState("Chennai"); // Selected city

  const topCities = ["Kolkata", "Chennai", "Bengaluru", "Mumbai", "New Delhi"];

  // Mapping of weather icon codes to corresponding icon URLs
  const weatherIcons = {
    'mist': 'https://awsweatherbucket.s3.ap-south-1.amazonaws.com/wi-fog.svg', // Add the URL for the Mist icon here
    'partly cloudy': 'https://awsweatherbucket.s3.ap-south-1.amazonaws.com/wi-day-cloudy.svg',
    'moderate rain shower': 'https://awsweatherbucket.s3.ap-south-1.amazonaws.com/wi-day-rain.svg', // Add the URL for the Moderate Rain Shower icon here
    'heavy rain shower': 'https://awsweatherbucket.s3.ap-south-1.amazonaws.com/wi-day-rain.svg', // Add the URL for the Heavy Rain Shower icon here
    'moderate or heavy rain shower': 'https://awsweatherbucket.s3.ap-south-1.amazonaws.com/wi-day-rain.svg', // Add the URL for the Moderate or Heavy Rain Shower icon here
    'light rain shower': 'https://awsweatherbucket.s3.ap-south-1.amazonaws.com/wi-day-rain.svg', // Add the URL for the Light Rain Shower icon here
    'sunny': 'https://awsweatherbucket.s3.ap-south-1.amazonaws.com/wi-day-sunny.svg', // Add the URL for the Sunny icon here
    'clear': 'URL_TO_CLEAR_ICON', // Add the URL for the Clear icon here
    'snow': 'https://awsweatherbucket.s3.ap-south-1.amazonaws.com/wi-snow.svg', // Add the URL for the Snow icon here
  };

  useEffect(() => {
    fetchWeatherData(cityName); // Fetch weather data for the current city on component mount
  }, [cityName]);

  const fetchWeatherData = (city) => {
    setLoading(true);
    setError(false);

    fetch(`http://13.233.116.30/api/get_weather?city=${city}`)
      .then((res) => {
        if (res.status === 200) {
          setError(false);
          return res.json();
        } else {
          throw new Error("Something went wrong");
        }
      })
      .then((data) => {
        setData(data);
      })
      .catch(() => setError(true))
      .finally(() => setLoading(false));
  };

  const handleSearch = (e) => {
    if (e.key === "Enter") {
      setCityName(inputText); // Update the cityName with the input text
      setInputText("");
    }
  };

  return (
    <div className="bg_img">
      <h1 className="top-cities-title">Top Cities</h1>
      <div className="top-cities">
        {topCities.map((city) => (
          <span
            key={city}
            className={`city-option ${city === selectedCity ? "selected" : ""}`}
            onClick={() => {
              setSelectedCity(city);
              setCityName(city); // Update the cityName when selecting a top city
            }}
          >
            {city}
          </span>
        ))}
      </div>

      {!loading ? (
        <>
          <TextField
            variant="filled"
            label="Search location"
            className="input"
            error={error}
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
            onKeyDown={handleSearch} // Use onKeyDown to trigger the search on "Enter" key press
          />
          <h1 className="city">{data.city}</h1>
          <div className="group">
            <h1>{data.weather.description}</h1>
            {/* Display weather icon */}
            <img
              src={
                weatherIcons[data.weather.description.toLowerCase()] ||
                weatherIcons[data.weather.icon] ||
                ""
              }
              alt="Weather Icon"
              onLoad={() => console.log("Weather icon loaded:", data.weather.icon)}
            />
          </div>
          <h1 className="temp">{data.main.temp} °C</h1>

          <Slide direction="right" timeout={800} in={!loading}>
            <div className="box_container">
              <div className="box">
                <p>Humidity</p>
                <h1>{data.main.humidity}%</h1>
              </div>
              <div className="box">
                <p>Wind Speed</p>
                <h1>{data.wind.speed} km/h</h1>
              </div>
              <div className="box">
                <p>Feels Like</p>
                <h1>{data.main.feels_like} °C</h1>
              </div>
            </div>
          </Slide>
        </>
      ) : (
        <CircularProgress />
      )}
    </div>
  );
}

export default App;
