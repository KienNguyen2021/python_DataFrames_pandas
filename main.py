import pandas

data = pandas.read_csv("weather_data.csv")

print(type(data))
print(data["day"])     # print index 0-12, and all temps

#convert data into dictionary :

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)         #  [12, 14, 15, 14, 21, 22, 24]
print(len(temp_list))    # 7

average = sum(temp_list) / len(temp_list)
print(average)              # the average temp : 17.428571428571427

print(data["temp"].mean())   # 17.428571428571427

print(data["temp"].max())   # Max temp : 24

print(data["condition"])
# the same :
print(data.condition)

# get data in Row :

print(data[data.day == "Monday"])        #  0  Monday    12     Sunny

# get maximum temp : data["temp"].max(), or :

print(data[data.temp == data.temp.max()])      #  6  Sunday    24     Sunny

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)          # convert temp into integer
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)                 # 53.6

