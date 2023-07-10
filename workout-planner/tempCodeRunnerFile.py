import requests
import datetime
WORKOUT_API_KEY = "585de0811ad59bc52195869a3504e026"
WORKOUT_API_ID = "5425bdbe"
WORKOUT_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/330744e1d4d3a822a82867281d86989a/googleWorkoutTracking/sheet1"
HEADER = {
    "x-app-id": WORKOUT_API_ID,
    "x-app-key": WORKOUT_API_KEY,
    "x-remote-user-id":  "0"
}
texts = input("How much did you workout today? ")
BODY = {
        "query": texts,
        "gender": "male",
        "weight_kg": 61,
        "height_cm": 170,
        "age": 20
}
rn = datetime.datetime.now()
month = str(rn.month)
if len(month) < 2:
    month = f"0{month}"
today_time = rn.time().strftime("%x")
today_date = f"{rn.day}/{month}/{rn.year}"
print(today_date)
response = requests.post(url=WORKOUT_API_ENDPOINT, json=BODY, headers=HEADER)
exercise_data = response.json()
# print(exercise_data)
exercise1 = exercise_data["exercises"]
# print(exercise1)
for exercise in exercise1:
    sheet_inputs = {
        "sheet1":
            {
                "date": today_date,
                "time": today_time,
                "exercise": exercise["name"].title(),
                "dura`tion": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
    resp = requests.post(SHEETY_URL, json=sheet_inputs)
print(resp.text)