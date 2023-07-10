import csv
import pandas as pd

# with open("./weather_data.csv") as file:
#     content = csv.reader(file)
#     temperature = []
#     for row in content:
#         temperature.append(row[1])
#     print(temperature[1:])
    
# file = pd.read_csv("./weather_data.csv")
# monday = file[file.day == "Monday"] 
# print(monday.temp*9/5 + 32)

data = {
    "students" : ["Jack", "John", "Jimmy"],
    "marks" : ["86","89","79"]
}

pd.DataFrame(data=data).to_csv("data.csv")
