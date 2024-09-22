# # import csv
# #
# # with open("weather_data.csv", mode="r") as data_file:
# #     # data = data_file.readlines()
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         print(row)
# #         if row[1]!="temp":
# #             temperature.append(int(row[1]))
# #     print(temperature)
# #
#
#
import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data)) #2D type dataframe
# print(type(data["temp"])) # 1D type series single column
# #sum(list) gives sum
# print(data["temp"].max())
# print(data.condition)
#
# print(data[data.day == "Monday"]) #row
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# mond_temp = monday.temp
# print(monday.temp)
# print(monday.temp[0])
#
# #pandas.Dataframe(dictionary) = data
# #data.to_csv(file name.csv) - new csv file created in the same folder

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"]=="Gray"]
grey_squirrels_count = len(grey_squirrels)
red_squirrels_count = len(data[data["Primary Fur Color"]=="Red"])
black_squirrels_count = len(data[data["Primary Fur Color"]=="Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
                "Fur Color":["Gray","Red","Black"],
                "Count" : [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

