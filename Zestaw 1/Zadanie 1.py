# Loading to Python Interpreter pandas package and import pandas library
import pandas as pd

# Read the file, name the columns
df = pd.read_csv("train.tsv", delimiter='\t',
                 names=["Value", "Number_Of_Rooms", "Area", "Floor_Number", "Address", "Description"])

# Calculate the average value and save as .csv
with open('out0.csv', 'w') as csvfile:
    csvfile.write(str(df["Value"].mean().round(0)))
