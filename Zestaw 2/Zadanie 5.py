# Loading to Python Interpreter pandas package and import pandas library
import pandas as pd
# Loading to Python Interpreter matplotlib package and import matplotlib library
import matplotlib.pyplot as plot
# Loading to Python Interpreter sklearn package, import linear_model and mean_squared_error library
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

# Read the files, select columns
df_public = pd.read_csv("survey_results_public.csv",
                        usecols=["Respondent", "Age", "YearsCode", "Age1stCode"],
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

# Checking types of objects in df_public dataframe.
type_obj = df_public.dtypes
print(type_obj)
print(df_public)

# Checking the correlation between the available data
print(df_public.corr(method='pearson'))

plot.scatter(df_public["Age"], df_public["YearsCode"])
plot.title("Years of coding depending on Age")
plot.xlabel("Age")
plot.ylabel("Years of coding")
plot.show()

plot.scatter(df_public["Age1stCode"], df_public["YearsCode"])
plot.title("Years of coding depending on Age of starting programming")
plot.xlabel("Age of starting programming")
plot.ylabel("Years of coding")
plot.show()

# Selected dependent variable: "YearsCode"
# Selected independent variables: "Age" & "Age1stCode"

# Removing outliers - using the method available in the file "regression-v0"
Q1 = df_public.quantile(0.25)
Q3 = df_public.quantile(0.75)
IQR = Q3 - Q1

df_public = df_public[~((df_public < (Q1 - 1.5 * IQR)) | (df_public > (Q3 + 1.5 * IQR))).any(axis=1)]
print(df_public)

# Create linear regression models and calculating MSE
reg1 = linear_model.LinearRegression()
reg1.fit(df_public[["Age"]], df_public["YearsCode"])
print("Coefficients: \n", reg1.coef_)
print("MSE: \n %.2f"
      % mean_squared_error(df_public["YearsCode"], reg1.predict(df_public[["Age"]])))

reg2 = linear_model.LinearRegression()
reg2.fit(df_public[["Age", "Age1stCode"]], df_public["YearsCode"])
print("Coefficients: \n", reg2.coef_)
print("MSE: \n %.2f"
      % mean_squared_error(df_public["YearsCode"], reg2.predict(df_public[["Age", "Age1stCode"]])))
