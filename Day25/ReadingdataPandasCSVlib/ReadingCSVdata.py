# 1. Method to retrieve but need to do a lot of word to clean the data
# with open("E:/Python/Day25/ReadingdataPandasCSVlib/weather_data.csv") as file:
#     data=file.readlines()
#     print(data)

# 2. Method use CSV inbuilt
# import csv

# with open("E:/Python/Day25//ReadingdataPandasCSVlib/weather_data.csv") as file:
#     data=csv.reader(file)
#     temp_list=[]
#     for i in data:
#         temp_list.append(i[1])
#     print(temp_list[1:])


import pandas
with open("E:/Python/Day25/ReadingdataPandasCSVlib/weather_data.csv") as file:
    data=pandas.read_csv(file)

    # print(data["temp"])
    # data_dic=data.to_dict()
    # print(data_dic)
    # temp_list=data["temp"].to_list()
    # print(temp_list)
    
    # # print(sum(temp_list)/len(temp_list))
    # # above same thing can be performed using pandas function as below
    # print (data["temp"].mean())
    # print(data["temp"].min())

    # get data in columms =-----Both work in same ways
    # print(data["condition"])
    # print(data.condition)

    # get data in rows
    # print(data[data.day=="Monday"])
    
    # to Print day which has max temp
    # print(data.day[data.temp==data["temp"].max()])

    # monday=data[data.day=="Monday"]
    # print(monday)
    # monday_temp_c=monday.temp
    # print(monday_temp_c)
    # in_f=monday_temp_c * 9/5 + 32
    # print(in_f)

    # Create  a data fram From python 
    student_dic={
        "students":["vishal","amit","aman"],
        "scores":[21,54,98]
    }
    dataF=pandas.DataFrame(student_dic)
    print(dataF)
    dataF.to_csv("newFile.csv")
