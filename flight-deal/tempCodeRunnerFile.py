def sheety(city, code):

#     for i in range(0,len(locs['prices'])):
#         if city == locs['prices'][i]['city']:
#             new_data = {
#                 "price":{
#                     "iataCode" : code
#                 }
#             }

#     for i in range(0,len(locs["prices"])):
#         if city == locs['prices'][i]['city']:
#             r = requests.put(url = f"{SHEETY}/{data[i]['id']}", json=new_data)
        
# # ----------------------------------------------------------------------------------------------------------------------

# # ----------------------------------------------------------------------------------------------------------------------
# #TEQUILLA
# # ----------------------------------------------------------------------------------------------------------------------
# def location():
#     data = locs['pricces']
#     for i in range(0,len(locs['prices'])):
#         loc_params = {
#             'term' :  locs['prices'][i]['city'],
#             'location_types' : 'city',
#         }
#         loc = requests.get(url = LOCATION_API, headers=loc_header, params = loc_params)
#         response_iata = loc.json()
#         sheety(data[i]['city'],response_iata['locations'][0]['code'])

# def forward():
#     month = dt.now().month + 6
#     year = dt.now().year 
#     if month > 12:
#         month = month - 12
#         year +=  1
#     frwd = f'{dt.now().day}/{month:02}/{year}'
#     return frwd

# today = dt.now().strftime('%d/%m/%Y')
# return_date = forward()

# for i in range(0,len(locs['prices'])):
#     search_params = {
#         'fly_from' : 'LON',
#         'fly_to' : locs['prices'][i]['iataCode'],
#         'date_from' : today,
#         'date_to' : return_date,
#         'curr' : 'INR'
#     }
#     travel = requests.get(url = SEARCH_API, headers = loc_header, params = search_params)
#     search_result = travel.json()
#     print(search_result)