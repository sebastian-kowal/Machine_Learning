# Loading to Python Interpreter pandas package and import pandas library
import pandas as pd
# Loading to Python Interpreter matplotlib package and import matplotlib library
import matplotlib.pyplot as plot

# Read the files, select columns
df_schema = pd.read_csv("survey_results_schema.csv")
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "Gender", "WorkWeekHrs", "CompTotal", "CurrencySymbol"],
                        index_col="Respondent")

# Check types of objects in df_survey dataframe.
type_obj = df_public.dtypes
print(type_obj)

# Check amount of columns and amount of rows.
print(df_public.shape)

# NULL records deletion and
df_public.dropna(inplace=True)

# Re-check amount of columns and amount of rows.
print(df_public.shape)

# Change type from float to int
# Omit this point because changing the data type is not possible, when in the data frame we have "Gender" column
# df_public = df_public.astype('int64', copy=False)
# print(df_public.dtypes)

# Creating a plot
plot.scatter(df_public["Age"], df_public["WorkWeekHrs"])
plot.title("Work Week Hours depending on Age")
plot.xlabel("Age")
plot.ylabel("Work Week Hours")
plot.show()

# Creating a second plot
df_public = df_public.loc[df_public["CurrencySymbol"] == "PLN"]
df = df_public[(df_public["Gender"] == "Man") | (df_public["Gender"] == "Woman")]
df = df[["Age", "Gender", "WorkWeekHrs", "CompTotal", "CurrencySymbol"]]

plot.scatter(df["Gender"], df["CompTotal"])
plot.title("Total Compensation depending on Gender")
plot.xlabel("Gender")
plot.ylabel("Total Compensation")
plot.show()
