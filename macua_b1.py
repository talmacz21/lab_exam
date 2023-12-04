import pandas as pd 
import pandas as pd
import csv

#Column titles in your .CSV file
col_list = ["Interval"]

#Read from file and seprate a specific column
data = pd.read_csv("words.csv", usecols=col_list)["Interval"]
#Change extracted data to a list
ls = list(data)
for n, item in enumerate(ls):
  #For example capitalize all words in list
	ls[n] = [str(item)range(30-0)]

#Show all changed data
for n, item in enumerate(ls):
  print(f"{n} : {item}")

  #Write changes to a new file
with open('b1_output.csv', "w") as s:
    w = csv.writer(s)
    for word in ls:
        w.writerow(word)
