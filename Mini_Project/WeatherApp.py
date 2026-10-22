#Build a Weather App using OpenWeather API.

import requests

API_KEY = "a4a92f58fbccd53b14abe0405a9bbc88"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL, params=params, timeout=10
        )

        if response.status_code == 404:
            print("City not found. Please check the name.")
            return

        if response.status_code == 401:
            print("Invalid API key or key not activated yet.")
            return

        response.raise_for_status()
        data = response.json()

        # Extract weather information
        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        description = data["weather"][0]["description"].title()

        # Display results
        print("\n===== WEATHER REPORT =====")
        print(f"City: {city_name}, {country}")
        print(f"Temperature: {temperature} °C")
        print(f"Feels Like: {feels_like} °C")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print("==========================")

    except requests.exceptions.Timeout:
        print("Request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Could not connect. Check your internet connection.")

    except requests.exceptions.RequestException as error:
        print("An API error occurred:", error)

    except (KeyError, IndexError, ValueError):
        print("Could not read the weather data.")


# Main program
while True:
    city = input("\nEnter city name (or type exit): ").strip()

    if city.lower() == "exit":
        print("Weather app closed.")
        break

    if not city:
        print("Please enter a city name.")
        continue

    get_weather(city)
