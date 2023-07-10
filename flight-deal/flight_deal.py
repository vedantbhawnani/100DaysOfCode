import requests
from datetime import datetime as dt
# ----------------------------------------------------------------------------------------------------------------------
#VARIABLES
# ----------------------------------------------------------------------------------------------------------------------
SHEETY = "https://api.sheety.co/8e2f819dc593e694f2a208e8e9f1333f/flightDeals/prices"
TEQUILLA_KEY = "VarKCda4nGfqgTD90GLtYm74vmPvX3J8"
SEARCH_API = "https://tequila-api.kiwi.com/search"
LOCATION_API = 'https://tequila-api.kiwi.com/locations/query'
# ----------------------------------------------------------------------------------------------------------------------

sheet = requests.get(SHEETY)
locs = sheet.json()
data = locs['prices']
# print(data)

loc_header = {
    "apikey" : TEQUILLA_KEY,
}
# ----------------------------------------------------------------------------------------------------------------------
#SHEETY
# ----------------------------------------------------------------------------------------------------------------------
def sheety(city, code):

    for i in range(0,len(data)):
        if city == data[i]['city']:
            new_data = {
                "price":{
                    "iataCode" : code
                }
            }

    for i in range(0,len(locs["prices"])):
        if city == data[i]['city']:
            r = requests.put(url = f"{SHEETY}/{data[i]['id']}", json=new_data)
        
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
#TEQUILLA
# ----------------------------------------------------------------------------------------------------------------------
def location():


    for i in range(0,len(locs['prices'])):
        loc_params = {
            'term' :  locs['prices'][i]['city'],
            'location_types' : 'city',
        }
        loc = requests.get(url = LOCATION_API, headers=loc_header, params = loc_params)
        response_iata = loc.json()
        sheety(data[i]['city'],response_iata['locations'][0]['code'])

def forward():
    month = dt.now().month + 6
    year = dt.now().year 
    if month > 12:
        month = month - 12
        year +=  1
    frwd = f'{dt.now().day}/{month:02}/{year}'
    return frwd

today = dt.now().strftime('%d/%m/%Y')

return_date = forward()

for i in range(0,len(data)):
    search_params = {
        'fly_from' : 'BOM',
        'fly_to' : data[i]['iataCode'],
        'date_from' : today,
        'date_to' : return_date,
        'curr' : 'INR'
    }
    travel = requests.get(url = SEARCH_API, headers = loc_header, params = search_params)
    search_result = travel.json()
    search_price = search_result['data'][0]['price']
    data_price = data[i]['lowestPrice']
    if data_price > search_price:
        print("UPDATE PRICE!")
        new_data = {
            'price' : {
                'lowestPrice' : search_price
            }
        }
        r = requests.put(url = f"{SHEETY}/{data[i]['id']}", json = new_data)
        print(r.text)
        