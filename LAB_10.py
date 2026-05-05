"""
## Q1

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

data = {
    "Study_Hours": [5, 8, 6, 7, np.nan, 4, 9, 10, 3, 6],
    "Attendance": [85, 90, np.nan, 88, 92, 75, 95, 98, 70, 80],
    "Previous_Grades": [78, 85, 80, 82, 88, 70, 91, 95, 65, 79],
    "Participation_Level": ["High", "Medium", "High", "Low", "Medium", "Low", "High", "High", "Low", "Medium"],
    "Internet_Usage": [3, 5, 4, 2, 6, 1, 5, 6, 2, 3],
    "Final_Score": [80, 88, 84, 79, 90, 68, 94, 97, 60, 81]
}

df = pd.DataFrame(data)

df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].mean())
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

le = LabelEncoder()
df["Participation_Level"] = le.fit_transform(df["Participation_Level"])

X = df.drop("Final_Score", axis=1)
y = df["Final_Score"]

print("Feature Importance Based on Correlation:")
print(df.corr()["Final_Score"].sort_values(ascending=False))

x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

LR = LinearRegression()

ModelLR = LR.fit(x_train, y_train)

PredictionLR = ModelLR.predict(x_test)

print("\nPredictions:")
print(PredictionLR)

mae = mean_absolute_error(y_test, PredictionLR)
rmse = np.sqrt(mean_squared_error(y_test, PredictionLR))
r2 = r2_score(y_test, PredictionLR)

print("\nModel Evaluation")
print("MAE:", mae)
print("RMSE:", rmse)

print("LR Testing Accuracy")
testingAccLR = r2 * 100
print(testingAccLR)

new_student = pd.DataFrame({
    "Study_Hours": [7],
    "Attendance": [89],
    "Previous_Grades": [84],
    "Participation_Level": [2],
    "Internet_Usage": [4]
})

predicted_score = ModelLR.predict(new_student)

print("\nPredicted Final Score for New Student:")
print(predicted_score[0])

"""
"""
## Q2
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

data = {
    "Income": [50000, 60000, np.nan, 80000, 30000, 45000, 70000, 90000, 35000, 40000],
    "Employment_Status": ["Employed", "Self-Employed", "Employed", "Unemployed", "Employed", "Self-Employed", "Employed", "Employed", "Unemployed", "Employed"],
    "Credit_Score": [700, 650, 720, 580, 600, 680, 750, 800, 590, np.nan],
    "Loan_Amount": [20000, 25000, 15000, 30000, 10000, 18000, 22000, 27000, 12000, 16000],
    "Marital_Status": ["Married", "Single", "Married", "Single", "Married", "Single", "Married", "Married", "Single", "Married"],
    "Loan_Approved": [1, 1, 1, 0, 0, 1, 1, 1, 0, 0]
}

df = pd.DataFrame(data)

df["Income"] = df["Income"].fillna(df["Income"].mean())
df["Credit_Score"] = df["Credit_Score"].fillna(df["Credit_Score"].mean())

le1 = LabelEncoder()
le2 = LabelEncoder()

df["Employment_Status"] = le1.fit_transform(df["Employment_Status"])
df["Marital_Status"] = le2.fit_transform(df["Marital_Status"])

X = df.drop("Loan_Approved", axis=1)
y = df["Loan_Approved"]

print("Feature Correlation with Target:")
print(df.corr()["Loan_Approved"].sort_values(ascending=False))

x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(x_train, y_train)

prediction = model.predict(x_test)

print("\nPredictions:")
print(prediction)

accuracy = accuracy_score(y_test, prediction) * 100
precision = precision_score(y_test, prediction) * 100
recall = recall_score(y_test, prediction) * 100
f1 = f1_score(y_test, prediction) * 100

print("\nModel Evaluation")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

new_applicant = pd.DataFrame({
    "Income": [55000],
    "Employment_Status": [1],
    "Credit_Score": [710],
    "Loan_Amount": [20000],
    "Marital_Status": [0]
})

result = model.predict(new_applicant)

print("\nLoan Approval Prediction for New Applicant:")
print(result[0])

"""

## Q3
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = {
    "Monthly_Charges": [70, 80, 65, 90, 50, 60, 85, 95, 55, 75],
    "Contract_Type": ["Month-to-Month", "One Year", "Month-to-Month", "Two Year", "Month-to-Month", "One Year", "Two Year", "Two Year", "Month-to-Month", "One Year"],
    "Tenure": [1, 24, 3, 36, 2, 12, 48, 60, 4, 18],
    "Internet_Service": ["Fiber", "DSL", "Fiber", "Fiber", "DSL", "DSL", "Fiber", "Fiber", "DSL", "DSL"],
    "Support_Calls": [5, 2, 6, 1, 7, 3, 2, 1, 6, 4],
    "Churn": [1, 0, 1, 0, 1, 0, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

df["Monthly_Charges"] = df["Monthly_Charges"].fillna(df["Monthly_Charges"].mean())
df["Tenure"] = df["Tenure"].fillna(df["Tenure"].mean())
df["Support_Calls"] = df["Support_Calls"].fillna(df["Support_Calls"].mean())

le1 = LabelEncoder()
le2 = LabelEncoder()

df["Contract_Type"] = le1.fit_transform(df["Contract_Type"])
df["Internet_Service"] = le2.fit_transform(df["Internet_Service"])

Q1 = df["Monthly_Charges"].quantile(0.25)
Q3 = df["Monthly_Charges"].quantile(0.75)
IQR = Q3 - Q1

df = df[(df["Monthly_Charges"] >= Q1 - 1.5 * IQR) & (df["Monthly_Charges"] <= Q3 + 1.5 * IQR)]

X = df.drop("Churn", axis=1)
y = df["Churn"]

scaler = StandardScaler()
X = scaler.fit_transform(X)

print("Feature Importance (Approx using correlation):")
print(df.corr()["Churn"].sort_values(ascending=False))

x_train, x_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = SVC(kernel="linear")

model.fit(x_train, y_train)

prediction = model.predict(x_test)

print("\nPredictions:")
print(prediction)

cm = confusion_matrix(y_test, prediction)
accuracy = accuracy_score(y_test, prediction) * 100
precision = precision_score(y_test, prediction) * 100
recall = recall_score(y_test, prediction) * 100
f1 = f1_score(y_test, prediction) * 100

print("\nConfusion Matrix:")
print(cm)

print("\nModel Evaluation")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

new_customer = pd.DataFrame({
    "Monthly_Charges": [78],
    "Contract_Type": [1],
    "Tenure": [10],
    "Internet_Service": [0],
    "Support_Calls": [4]
})

new_customer = scaler.transform(new_customer)

result = model.predict(new_customer)

print("\nChurn Prediction for New Customer:")
print(result[0])
