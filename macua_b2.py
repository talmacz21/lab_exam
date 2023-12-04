import pandas as pd 
import pandas as pd
import csv

#Column titles in your .CSV file
col_list = ["Interval"]
df = pd.read_csv('Exam_Table.csv', na_values='*')
    grouped = df.groupby('Genus')
        grouped [str(St)]
  print (Genus:', np.mean[df['Genus'], St]')
     print (df)

#create a new file
df.to_csv('b_output2.csv', index=False)
# source:
https://justinbois.github.io/bootcamp/2021/lessons/l18_split_apply_combine.html