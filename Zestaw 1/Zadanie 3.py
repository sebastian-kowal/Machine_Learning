# Loading to Python Interpreter pandas package and import pandas library
import pandas as pd

# Read the files, name the columns
df = pd.read_csv("train.tsv", delimiter='\t',
                 names=["Value", "Number_Of_Rooms", "Area", "Floor_Number", "Address", "Description"])

df2 = pd.read_csv("description.csv", delimiter=',')

# Combining the second data frame with the first data frame adding a new column
df = pd.merge(df, df2, left_on="Floor_Number", right_on="liczba", how="left")

# Create dataframe with selected columns (I do this because both columns from the file 'description' are displayed)
df3 = pd.DataFrame(df, columns=["Value", "Number_Of_Rooms", "Area", "Floor_Number", " opis", "Address", "Description"])

# Save as a .csv file
with open('out2.csv', 'w', encoding="utf-8") as csvfile:
    df3.to_csv(csvfile, index=False, line_terminator='\n')
