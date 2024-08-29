import requests
from twilio.rest import Client

api_key = "ec027a9379160f18edb12445efdd6157"
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

account_sid = "ACb40a6e3ac3054e2745bc4a6b79c45083"
auth_token = "e5d8b3f1cbb4f6ca8610a49a8fb3eda4"


weather_params = {
    "lat": 22.572645,                                                               # Lat of kolkata
    "lon": 88.363892,                                                               # Lon of Kolkata
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(api_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

#id = weather_data["list"][0]["weather"][0]["id"]

will_rain = False
for hour_data in weather_data["list"]:
    condition_id = hour_data["weather"][0]["id"]

    if int(condition_id) < 700:                                                 # Condition for rain in id code
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)                                    # Using twilio to send message whenever it rains

    message = client.messages.create(
        body="Bring an Umbrella, It's gonna rain.",
        from_="+12566769328",
        to="+919903795169",
    )

    print(message.status)