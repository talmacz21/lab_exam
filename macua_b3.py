import pandas as pd
df = pd.read_csv('Exam_Table.csv', na_values='*')
df[genus] = df [species]
 print (df)
#create a new file
df.to_csv('b_output3.csv', index=False)
#source: 
https://justinbois.github.io/bootcamp/2021/lessons/l18_split_apply_combine.html