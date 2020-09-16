# Loading to Python Interpreter packages and import libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

# Read the file, name the columns
df = pd.read_csv("train.tsv", delimiter="\t",
                 names=["Occupancy", "Date", "Temperature", "Humidity", "Light", "CO2", "HumidityRatio"])

# NULL records deletion
df.dropna(inplace=True)

df.describe()

# Logistic regression classifier on one independent variable: "Temperature"
reg = LogisticRegression()
x_train = df[["Temperature"]]
y_train = df.Occupancy

reg.fit(x_train, y_train)
y_train_pred = reg.predict(x_train)

# Calculation "Occupancy"
occupancy_percentage = sum(df["Occupancy"]) / len(df)
print("Occupancy percentage is:\n" + str(occupancy_percentage))

# Calculation "Compute confusion matrix" for zero rule model
cm = confusion_matrix(y_train, np.zeros(len(y_train)))
total = sum(sum(cm))

# Calculation "Accuracy", "Sensitivity" and "Specificity" values for zero rule model
print("Zero rule model accuracy on training set is:\n"
      + str(1 - occupancy_percentage))
# Another way to calculation "Accuracy"
acc = (cm[0, 0]+cm[1, 1])/total
print("Zero rule model accuracy on training set is:\n", acc)

sensitivity = cm[0, 0]/(cm[0, 0]+cm[0, 1])
print("Zero rule model sensitivity on training set is:\n", sensitivity)

specificity = cm[1, 1]/(cm[1, 0]+cm[1, 1])
print("Zero rule model specificity on training set is:\n", specificity)

# Calculation "Compute confusion matrix" for logisitic regression model
cm = confusion_matrix(y_train, y_train_pred)
total = sum(sum(cm))

# Calculation "Accuracy", "Sensitivity" and "Specificity" values for logisitic regression model
reg_accuracy = sum(y_train == y_train_pred) / len(df)
print("Training set accuracy for logistic regression model "
      + "on Temperature variable:\n" + str(reg_accuracy))
# Another way to calculation "Accuracy"
reg_acc = (cm[0, 0]+cm[1, 1])/total
print("Training set accuracy for logistic regression model "
      + "on Temperature variable:\n" + str(reg_acc))

reg_sensitivity = cm[0, 0]/(cm[0, 0]+cm[0, 1])
print("Training set sensitivity for logistic regression model "
      + "on Temperature variable:\n" + str(reg_sensitivity))

reg_specificity = cm[1, 1]/(cm[1, 0]+cm[1, 1])
print("Training set specificity for logistic regression model "
      + "on Temperature variable:\n" + str(reg_specificity))

# Logistic regression classifier on one independent variable: "Temperature" - test set
df_column_name = ["Date", "Temperature", "Humidity", "Light", "CO2", "HumidityRatio"]
x_column_name = ["Temperature"]

# Read the file, select columns
x_test = pd.read_csv("test.tsv", sep='\t', names=df_column_name, usecols=x_column_name)

# Read the file, select columns
df_result = pd.read_csv("results.tsv", sep='\t', names=["y"])
df_result["y"] = df_result["y"].astype("category")

y_true_test = df_result["y"]
y_test_predict = reg.predict(x_test)

# Calculation "Compute confusion matrix" for logisitic regression model
cm_test = confusion_matrix(y_true_test, y_test_predict)
total = sum(sum(cm_test))

# Calculation "Accuracy", "Sensitivity" and "Specificity" values for test set
test_accuracy = accuracy_score(y_true_test, y_test_predict)
print("Accuracy on test dataset (temperature variable):\n" + str(test_accuracy))
# Another way to calculation "Accuracy"
test_acc = (cm_test[0, 0] + cm_test[1, 1])/total
print("Accuracy on test dataset (temperature variable):\n" + str(test_acc))

test_sensitivity = cm_test[0, 0]/(cm_test[0, 0]+cm_test[0, 1])
print("Sensitivity on test dataset (temperature variable):\n" + str(test_sensitivity))

test_specificity = cm_test[1, 1]/(cm_test[1, 0]+cm_test[1, 1])
print("Specificity on test dataset (temperature variable):\n" + str(test_specificity))

# Save the y_test_predict
df_save = pd.DataFrame(y_test_predict)
df_save.to_csv("out0.csv", index=False, header=False)

# Logistic regression classifier on all but date independent variables
reg_all = LogisticRegression()
x_train_all = df[["Temperature", "Humidity", "Light", "CO2", "HumidityRatio"]]
reg_all.fit(x_train_all, y_train)

y_train_pred_all = reg_all.predict(x_train_all)

# Calculation "Compute confusion matrix" for logisitic regression model
conf_matrix = confusion_matrix(y_train, y_train_pred_all)
total = sum(sum(conf_matrix))

# Calculation "Accuracy", "Sensitivity" and "Specificity" values for logisitic regression model
reg_all_accuracy = accuracy_score(y_train, y_train_pred_all)
print("Training set accuracy for logistic regression model " +
      "on all but date variable:\n" + str(reg_all_accuracy))
# Another way to calculation "Accuracy"
reg_all_acc = (conf_matrix[0, 0]+conf_matrix[1, 1])/total
print("Training set accuracy for logistic regression model " +
      "on all but date variable:\n" + str(reg_all_acc))

reg_all_sensitivity = conf_matrix[0, 0]/(conf_matrix[0, 0]+cm[0, 1])
print("Training set sensitivity for logistic regression model " +
      "on all but date variable:\n" + str(reg_all_sensitivity))

reg_all_specificity = conf_matrix[1, 1]/(conf_matrix[1, 0]+conf_matrix[1, 1])
print("Training set specificity for logistic regression model "
      + "on all but date variable:\n" + str(reg_all_specificity))

# Logistic regression classifier on all but date independent variables - test set
df_column_names = ["Date", "Temperature", "Humidity", "Light", "CO2", "HumidityRatio"]
x_column_names = ["Temperature", "Humidity", "Light", "CO2", "HumidityRatio"]

# Read the file, select columns
x_test1 = pd.read_csv("test.tsv", sep='\t', names=df_column_names, usecols=x_column_names)

# Read the file, select columns
df_results = pd.read_csv("results.tsv", sep='\t', names=["y"])
df_results["y"] = df_results["y"].astype("category")

y_true = df_results["y"]
y_test_pred = reg_all.predict(x_test1)

# Calculation "Compute confusion matrix" for logisitic regression model
cm_test1 = confusion_matrix(y_true, y_test_pred)
total = sum(sum(cm_test1))

# Calculation "Accuracy", "Sensitivity" and "Specificity" values for test set
test1_accuracy = accuracy_score(y_true, y_test_pred)
print("Accuracy on test dataset (full model):\n" + str(test1_accuracy))
# Another way to calculation "Accuracy"
test1_acc = (cm_test1[0, 0] + cm_test1[1, 1])/total
print("Accuracy on test dataset (full model):\n" + str(test1_acc))

test1_sensitivity = cm_test1[0, 0]/(cm_test1[0, 0]+cm_test1[0, 1])
print("Sensitivity on test dataset (full model):\n" + str(test1_sensitivity))

test1_specificity = cm_test1[1, 1]/(cm_test1[1, 0]+cm_test1[1, 1])
print("Specificity on test dataset (full model):\n" + str(test1_specificity))
