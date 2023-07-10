import requests

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall?lat=19.159963443072066&lon=72.83627812417761&exclude=minutely,current,daily&appid=69f04e4613056b159c2761a9d9e664d2")
response.raise_for_status()
data = response.json()

# print(data)
count = 0
for i in range(0,12):
    id = data['hourly'][i]['weather'][0]['id']
    if id<700:
        print("Bring an umbrella")
        count += 1
        break
    
if count == 0:
    print("good to go")