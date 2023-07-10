import pandas as pd

data = pd.read_csv("nato.csv")

nato = {row.letter : row.code for (index, row) in data.iterrows()}

user = input("Enter a name: ").upper()

coded = [nato[letter] for letter in user if letter in nato.keys()]
print(coded)