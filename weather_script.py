import requests

# Fetch weather data from OpenWeatherMap API

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        weather_description = weather['description']
        
        print(f"Temperature: {temperature}")
        print(f"Pressure: {pressure}")
        print(f"Humidity: {humidity}")
        print(f"Weather description: {weather_description}")
    else:
        print("City not found.")

def main():
    api_key = "your_api_key_here"  # Replace with your actual API key
    city = input("Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
