# Load the CSV data into a DataFrame
from pkg_resources import ExtractionError
with open("./Exam_Table.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
         print(row)
#extract rows
ExtractionError ;row (30,0)
print(row)