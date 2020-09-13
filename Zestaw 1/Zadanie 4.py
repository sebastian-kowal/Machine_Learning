# Loading to Python Interpreter pandas package and import pandas library
import pandas as pd

# Read the files, select columns
df_schema = pd.read_csv("survey_results_schema.csv")
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "WorkWeekHrs", "CompTotal"],
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
df_public = df_public.astype('int64', copy=False)
print(df_public.dtypes)
