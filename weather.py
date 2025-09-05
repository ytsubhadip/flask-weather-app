import requests
def weather_fetch(city):
    from config import api_key
    url= f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    r = requests.get(url)
    data = r.json()
    temp = (data["main"]["temp"])
    temp = temp - 273.15
    temp = round(temp)
    city = data["name"]
    data = [temp,city]
    return data

if __name__ == "__main__":
    print(weather_fetch("kolkata"))