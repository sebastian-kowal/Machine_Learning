# Loading to Python Interpreter pandas package and import pandas library
import pandas as pd

# Read the files, select columns
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Student", "Age", "Gender", "WorkWeekHrs", "CompTotal", "YearsCode", "Age1stCode"],
                        index_col="Respondent")

# NULL records deletion
df_public.dropna(inplace=True)

# Converting text data to numeric data
df_public.loc[df_public["YearsCode"] == "Less than 1 year"] = 0
df_public.loc[df_public["YearsCode"] == "More than 50 years"] = 55
df_public.loc[df_public["Age1stCode"] == "Younger than 5 years"] = 0
df_public.loc[df_public["Age1stCode"] == "Older than 85"] = 90

# Change type to float / string
df_public["YearsCode"] = df_public["YearsCode"].astype("float64")
df_public["Age1stCode"] = df_public["Age1stCode"].astype("float64")
df_public["Gender"] = df_public["Gender"].astype("str")

# Checking types of objects in df_public dataframe.
type_obj = df_public.dtypes
print(type_obj)

# Converting text data to numeric data
student_map = {"Yes, full-time": 1, "Yes, part-time": 1, "No": 0}
df_public["Student"] = df_public["Student"].map(student_map)

# One-Hot Encoding
df_public = df_public[(df_public["Gender"] == "Man") | (df_public["Gender"] == "Woman")]
df_public = pd.get_dummies(df_public, columns=["Gender"])
print(df_public)

# Checking the correlation between the available data
print(df_public.corr(method='pearson'))

# Removing outliers - using the method available in the file "regression-v0"
Q1 = df_public.quantile(0.25)
Q3 = df_public.quantile(0.75)
IQR = Q3 - Q1

df_public = df_public[~((df_public < (Q1 - 1.5 * IQR)) | (df_public > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df_public)
