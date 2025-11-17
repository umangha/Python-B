import pandas as pd

data = pd.read_csv("./Assignments/Day-25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251116.csv")


FurColor = data['Primary Fur Color'].value_counts()
print(FurColor)
# FurColor.to_csv("./FurColorSquirrel.csv")

