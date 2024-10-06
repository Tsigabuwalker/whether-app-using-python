import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Default to metric
    }
    response = requests.get(base_url, params=params)
    return response.json()

def get_forecast(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def determine_condition(weather_data):
    if weather_data['cod'] != 200:
        return "City not found."

    main_weather = weather_data['weather'][0]['main'].lower()
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']

    condition_message = f"Weather: {main_weather.capitalize()}\n"
    condition_message += f"Temperature: {temperature}°C\n"
    condition_message += f"Humidity: {humidity}%\n"
    condition_message += f"Wind Speed: {wind_speed} m/s\n"

    if 'clear' in main_weather:
        condition_message += "It's sunny!"
    elif 'rain' in main_weather:
        condition_message += "It's raining!"
    elif 'snow' in main_weather:
        condition_message += "It's snowing!"
    elif 'cloud' in main_weather:
        condition_message += "It's cloudy!"
    else:
        condition_message += "Weather condition is: " + main_weather.capitalize()

    return condition_message

def display_forecast(forecast_data):
    if forecast_data['cod'] != '200':
        return "City not found."

    forecast_message = "5-Day Forecast:\n"
    for entry in forecast_data['list']:
        date = entry['dt_txt']
        temp = entry['main']['temp']
        weather_desc = entry['weather'][0]['description']
        forecast_message += f"{date}: {temp}°C, {weather_desc}\n"
    
    return forecast_message

def main_menu():
    print("Welcome to the Weather Condition Checker!")
    print("1. Check Current Weather")
    print("2. Check 5-Day Weather Forecast")
    print("3. Exit")

def main():
    api_key = 'your_api_key_here'  # Replace with your actual API key
    while True:
        main_menu()
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            city = input("Enter the city name: ")
            weather_data = get_weather(city, api_key)
            condition = determine_condition(weather_data)
            print(condition)
        
        elif choice == '2':
            city = input("Enter the city name: ")
            forecast_data = get_forecast(city, api_key)
            forecast = display_forecast(forecast_data)
            print(forecast)
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()