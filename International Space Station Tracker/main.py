import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 22.572645      # latitude of kolkata
MY_LONG = 88.363892     # longitude of kolkata

MY_EMAIL = "abhiruptest12@gmail.com"
PASSWORD = "qlwfxybawtngihoh"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")          # ISS API Overhead URL
    response.raise_for_status()
    data = response.json()                                                          # Storing the data of the json in data

    iss_latitude = float(data["iss_position"]["latitude"])                          # Accessing the lat from the data
    iss_longitude = float(data["iss_position"]["longitude"])                        # Accessing the long from the data

    # Position of my lat or long is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()                                                                       # Return status if any error
    data = response.json()                                                                            # Storing the json data in data
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])                             # Sunrise time
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])                               # Sunset time

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:                                                     # Checking if it's night time
        return True

while True:

    time.sleep(60)                                                                                    # This will refresh and run this code every 60 secs

    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="abhirupsinha@yahoo.com",
                            msg="Subject: Look Up\n\nLook Up, ISS is above you in the sky.")






