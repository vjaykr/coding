import pandas as pd 
from matplotlib import pyplot as plt

df = pd.read_csv('D:\\CODE\\5th_Semester\\DVDA\\insurance_data.csv')
print(df.head())
print('.........................................................................................')
plt.scatter(df.age,df.bought_insurance,marker='+',color='red')
plt.show()
print('.........................................................................................')
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)
print(X_train)

print('.........................................................................................')

print(X_test)
print('.........................................................................................')
print(y_train)
print('.........................................................................................')
print(y_test)
print('.........................................................................................')

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)
print(y_predicted)
print('.........................................................................................')
model.predict_proba(X_test)
print('.........................................................................................')
print(model.score(X_test,y_test))
print(model.coef_)
print('.........................................................................................')
print(model.intercept_)
print('.........................................................................................')
print('after math')
import math
def sigmoid(x):
  return 1 / (1 + math.exp(-x))
def prediction_function(age):
    z = 0.329 * age - 10.16
    y = sigmoid(z)
    return y
age = 35
print(prediction_function(age))
print('.........................................................................................')
age = 43
print(prediction_function(age))

x = range(0, 50)
y = [prediction_function(i) for i in x]

plt.plot(x, y)
plt.title('S-shaped Curve')
plt.xlabel('Age')
plt.ylabel('Probability')
plt.grid(True)
plt.show()