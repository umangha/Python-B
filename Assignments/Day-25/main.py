
# with open("./Assignments/Day-25/weather_data.csv") as data:
#     weather_data = data.readlines()
#     print(weather_data)

###############################

# ## Using the inbuilt csv 
# import csv

# with open("./Assignments/Day-25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))

# print(temperatures)

##########################
## Using the padas library to the above

import pandas

data=pandas.read_csv("./Assignments/Day-25/weather_data.csv")
# print(data)

# Converting the temp to list
temp_list=data["temp"].tolist()
# print(temp_list)

# ## Average of temp
# sum_of_list = sum(temp_list)
# no_of_item = len(temp_list)
# avg = sum_of_list/no_of_item
# print("%.2f"%avg)

# ## Alternative using Pandas Series
# print(data["temp"].mean())

# ## Max Value of temp
# print(data["temp"].max())

# ## Finding the row in which temp was max
# # max_data =data["temp"].max()
# # print(data.loc[data["temp"] == max_data])

# # Does the same
# print(data[data.temp == data.temp.max()])

# ## Find the temp in fahrenheight instead of celcius in monday
# monday = data[data.day == "Monday"]
# temp_in_C = monday.temp
# temp_in_f = temp_in_C*(9/5)+32
# print(temp_in_C)
# print(temp_in_f)

##############################
data_dict = {
    "Key": [1,2,3],
    "Student":["Yujan","Ram","Sagar"]
}

df =pandas.DataFrame(data_dict)

# # Save to csv
# df.to_csv("./roll_stu.csv")
