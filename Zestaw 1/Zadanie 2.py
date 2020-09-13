# Loading to Python Interpreter pandas package and import pandas library
import pandas as pd

# Read the file, name the columns
df = pd.read_csv("train.tsv", delimiter='\t',
                 names=["Value", "Number_Of_Rooms", "Area", "Floor_Number", "Address", "Description"])

# Adding a price per square meter column
df["Value_of_suqare_meter"] = df["Value"]/df["Area"]

# Select rows from Data Frame
rooms = df["Number_Of_Rooms"] >= 3
price = df["Value_of_suqare_meter"] < df["Value_of_suqare_meter"].mean()

# Create dataframe with selected rows and with selected columns.
df2 = pd.DataFrame(df[rooms & price], columns=["Number_Of_Rooms", "Value", "Value_of_suqare_meter"])

# Save selected columns as a .csv file
with open('out1.csv', 'w', encoding="utf-8") as csvfile:
    df2.to_csv(csvfile, index=False, line_terminator='\n')
