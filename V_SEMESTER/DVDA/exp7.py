import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree

# Read the CSV file
df = pd.read_csv('titanic.csv')

# Print the first few rows of the dataframe
print(df.head())

# Prepare the inputs and target variables
inputs = pd.get_dummies(df.drop('Survived', axis='columns'))
target = df['Survived']

# Encode categorical variables
le_sex = LabelEncoder()
le_embarked = LabelEncoder()

inputs['Sex_n'] = le_sex.fit_transform(inputs['Sex'])
inputs['Embarked_n'] = le_embarked.fit_transform(inputs['Embarked'])

# Drop the original categorical variables
inputs.drop(['Sex', 'Embarked'], axis='columns', inplace=True)

# Train the decision tree classifier
model = tree.DecisionTreeClassifier()
model.fit(inputs, target)

# Evaluate the model
score = model.score(inputs, target)
print("Model accuracy:", score)

# Make predictions
predictions = model.predict([[3, 1, 22, 0, 7.25, 2]])
print("Predictions:", predictions)
