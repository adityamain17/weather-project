import requests

# Input section
city_name = input("Enter the city name: ")
Api_key = input("Enter your API key: ")

# API call
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Api_key}&units=metric"
response = requests.get(url)

# Response handling
if response.status_code == 200:
    data = response.json()
    
    weather = data["weather"][0]["description"].title()
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    
    print("\n🌤️  Weather Report")
    print("────────────────────────────")
    print(f"City: {city_name.title()}")
    print(f"Weather: {weather}")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print("────────────────────────────")
    print("✅ Thank You for Visiting! ☀️\n")
else:
    print("\ Failed to fetch weather data.")
    print("Please check your city name or API key.\n")
