import pandas as pd

data = pd.read_csv("squirrel_data.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

dic = {
    "Fur Color" : ["Grey", "Cinnamon", "Black"],
    "Count" : [gray, cinnamon, black]
}

pd.DataFrame(data= dic).to_csv("squirrel_reduced.csv")