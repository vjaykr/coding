import pandas as np
exp2 = np.read_excel('D:\\CODE\\5th_Semester\\DVDA\\Students.xlsx')
print(exp2)



mean = exp2['Age'].mean()
print(mean)

median = exp2['Age'].median()
print(median)

mode = exp2['Age'].mode()
print(mode)


rangee = exp2['Age'].max() - exp2['Age'].min()
print(rangee)


# Calculate the lower and upper bounds for outliers
Q1 = exp2['Age'].quantile(0.25)
Q3 = exp2['Age'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers in the Age column
outliers = exp2[(exp2['Age'] < lower_bound) | (exp2['Age'] > upper_bound)]
print(outliers)