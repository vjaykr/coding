import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt

exp3 = pd.read_csv('D:/CODE/5th_Semester/DVDA/homeprices.csv')

print(exp3)
print("Shape of the data:")
print(exp3.shape)
print("Size of the data:")
print(exp3.isnull().sum())
print("Correlation of the data:")
print(exp3.corr())
print(exp3.drop('price', axis=1))

x = exp3.drop('price', axis=1)
y = exp3['price']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=40)
print("X_train shape is", X_train.shape)

lr = LinearRegression()
lr.fit(X_train, y_train)

y_train_pred = lr.predict(X_train)
y_test_pred = lr.predict(X_test)

print("lr score on training data:", lr.score(X_train, y_train))
print("lr score on test data:", lr.score(X_test, y_test))
