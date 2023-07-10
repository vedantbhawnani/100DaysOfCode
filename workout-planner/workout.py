import requests
from datetime import datetime 

KEY = "585de0811ad59bc52195869a3504e026"
ID = "5425bdbe"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

header = {
    "x-app-id" : ID,
    "x-app-key" : KEY,
    "x-remote-user-id" : "0",
}

workout = input("What workout did you do today? ")

param = {
 "query": workout,
 "gender":"male",
 "weight_kg": 53.3,
 "height_cm" : 180,
 "age":19
}



r = requests.post(url = URL, headers= header, json = param)
data = r.json()

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "workout" : {
            "date" : today,
            "time" : now,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"], 
        }
    }

    sheet = requests.post(url = "https://api.sheety.co/785733f13ed7d953c6f854c7b9036a49/myWorkouts/workout", json = sheet_inputs)

    print(sheet.text)