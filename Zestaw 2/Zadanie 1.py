# Loading to Python Interpreter pandas package and import pandas library
import pandas as pd
# Loading to Python Interpreter matplotlib package and import matplotlib library
import matplotlib.pyplot as plot

# Read the files, select columns
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "WorkWeekHrs", "CompTotal", "YearsCode", "Age1stCode"],
                        index_col="Respondent")

# NULL records deletion
df_public.dropna(inplace=True)

# Converting text data to numeric data
df_public.loc[df_public["YearsCode"] == "Less than 1 year"] = 0
df_public.loc[df_public["YearsCode"] == "More than 50 years"] = 55
df_public.loc[df_public["Age1stCode"] == "Younger than 5 years"] = 0
df_public.loc[df_public["Age1stCode"] == "Older than 85"] = 90

# Change type to float
df_public["YearsCode"] = df_public["YearsCode"].astype("float64")
df_public["Age1stCode"] = df_public["Age1stCode"].astype("float64")

# Checking types of objects in df_public dataframe.
type_obj = df_public.dtypes
print(type_obj)

# Checking the correlation between the available data
print(df_public.corr(method='pearson'))

# Creating a plots
plot.scatter(df_public["Age"], df_public["WorkWeekHrs"])
plot.title("Work Week Hours depending on Age")
plot.xlabel("Age")
plot.ylabel("Work Week Hours")
plot.show()

plot.scatter(df_public["Age"], df_public["CompTotal"])
plot.title("Total Compensation depending on Age")
plot.xlabel("Age")
plot.ylabel("Total Compensation")
plot.show()

plot.scatter(df_public["Age"], df_public["YearsCode"])
plot.title("Years of coding depending on Age")
plot.xlabel("Age")
plot.ylabel("Years of coding")
plot.show()

plot.scatter(df_public["Age"], df_public["Age1stCode"])
plot.title("Age of starting programming depending on Age")
plot.xlabel("Age")
plot.ylabel("Age of starting programming")
plot.show()

plot.scatter(df_public["WorkWeekHrs"], df_public["CompTotal"])
plot.title("Total Compensation depending on Work Week Hours")
plot.xlabel("Work Week Hours")
plot.ylabel("Total Compensation")
plot.show()

plot.scatter(df_public["YearsCode"], df_public["CompTotal"])
plot.title("Total Compensation depending on Years of coding")
plot.xlabel("Years of coding")
plot.ylabel("Total Compensation")
plot.show()

plot.scatter(df_public["YearsCode"], df_public["WorkWeekHrs"])
plot.title("Work Week Hours depending on Years of coding")
plot.xlabel("Years of coding")
plot.ylabel("Work Week Hours")
plot.show()

plot.scatter(df_public["Age1stCode"], df_public["CompTotal"])
plot.title("Total Compensation depending on Age of starting programming")
plot.xlabel("Age of starting programming")
plot.ylabel("Total Compensation")
plot.show()

plot.scatter(df_public["Age1stCode"], df_public["WorkWeekHrs"])
plot.title("Work Week Hours depending on Age of starting programming")
plot.xlabel("Age of starting programming")
plot.ylabel("Work Week Hours")
plot.show()

plot.scatter(df_public["Age1stCode"], df_public["YearsCode"])
plot.title("Years of coding depending on Age of starting programming")
plot.xlabel("Age of starting programming")
plot.ylabel("Years of coding")
plot.show()

# Selected dependent variable: "YearsCode"
# Selected independent variables: "Age" & "Age1stCode"
