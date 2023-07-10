import requests
import datetime as dt
import smtplib
import time

def is_above():
    if 14.159963443072066< iss_latitude<24.159963443072066 and 67.83627812417761<iss_longitude<77.83627812417761:
        return True
        

response= requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

LAT = 19.159963443072066
LONG =  72.83627812417761
mail = "testcheck366@gmail.com"
password = "qozkqbosdlrydoue"

iss_latitude = float(data["iss_position"]["latitude"]) 
iss_longitude = float(data["iss_position"]["longitude"])

iss_position = (iss_latitude, iss_longitude)

parameters = {
    "lat": LAT,
    "long" : "LONG",
    "formatted" : 0,
}

def is_dark():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = dt.now()

    if now<=sunrise and now>=sunset:
        return True

while time.sleep(60):
    if is_above() and is_dark:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=mail, password=password)
            connection.sendmail(
                from_addr=mail, 
                to_addrs="siddhishettyspam@gmail.com", 
                msg=f"Subject: ISS! ISS! \n\n ISS is above within 5 degrees of you. LOOK UP LOOK UP!"
            )