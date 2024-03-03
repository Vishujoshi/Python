import pandas

with open("E:/Python/Day25/Squireeldata/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240229.csv") as file:
    data=pandas.read_csv(file)
    gray_c=(sum(data["Primary Fur Color"]=="Gray"))
    black_c=(sum(data["Primary Fur Color"]=="Black"))
    Cinnamon_c=(sum(data["Primary Fur Color"]=="Cinnamon"))


data_dic={
    "Fur Color" : ["Gray","Black","Cinnamon"],
    "Count" : [gray_c,black_c,Cinnamon_c]

    }

dataCSV=pandas.DataFrame(data_dic)
print(dataCSV)
dataCSV.to_csv("mydata.csv")