import requests





print("=======================\n"
      "Weatherly - Weather App\n"
      "=======================\n")

api_key = ""
lat = -26.2041  # Latitude of Johannesburg, South Africa
lon = 28.0473   # Longitude of Johannesburg, South Africa
#city_name = "Lubumbashi"

city_name = input('Search City: ')

#url = f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={api_key}&include=minutely"
url = f"https://api.weatherbit.io/v2.0/current?city={city_name}&key={api_key}&include=minutely"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data['data'][0]['temp']
    city = data['data'][0]['city_name']
    clouds = data['data'][0]['clouds']
    gust = data['data'][0]['gust']
    snow = data['data'][0]['snow']
    sunrise = data['data'][0]['sunrise']
    sunset = data['data'][0]['sunset']
    #sky = data['data'][0]['description']
    print(f"The temperature is {temperature} degrees Celsius\n"
          f"City: {city}\n"
          f"Clouds: {clouds}\n"
          f"Gust: {gust}\n"
          f"Snow: {snow}\n"
          f"Sunrise: {sunrise}\n"
          f"Sunset: {sunset}\n")
          #f"Sky: {sky}")
else:
    print(f"Failed to fetch data: {response.status_code}")
print(url)
