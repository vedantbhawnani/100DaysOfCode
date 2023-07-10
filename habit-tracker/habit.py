import requests
import datetime as dt

TOKEN = "asdkfjh23sad"

#STEP 1
# user = 'https://pixe.la/v1/users '
# set_params = {
#     "token" : TOKEN,
#     "username" : "impulseee",
#      "agreeTermsOfService" : "yes",
#      "notMinor" : "yes", 
# }

# r = requests.post(url = user, json = set_params)

# #STEP 2
# post_graph = 'https://pixe.la/v1/users/impulseee/graphs'

# graph_param = {
#     "id" : "graph1",
#     "name": "productive",
#     "unit" : "hours",
#     "type" : "float",
#     "color" : "kuro",
#     "timezone" : "Asia/Kolkata",
# }

# header = {
#     "X-USER-TOKEN" : TOKEN,
# }

# r = requests.post(url = post_graph, json = graph_param, headers = header)
# print(r.text)

#STEP 3
# graph = 'https://pixe.la/v1/users/impulseee/graphs/graph1'

#STEP 4
pixel = 'https://pixe.la/v1/users/impulseee/graphs/graph1'
header = { 
    "X-USER-TOKEN" : TOKEN,
}

today = dt.datetime.now()
print(today.strftime("%Y%m%d"))

param = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How productive were you today?"),
}

r = requests.post(url = pixel, headers= header, json = param)
print(r.text)