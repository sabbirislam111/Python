import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv('HR_comma_sep.csv')

'''
Search
    1. kaggle hr dataset
    2. pandas replece  string to number
    3. panda get dummies
    4. matplotlib
    5. sitkits learn logistic regression
    6. sitkit learn split dataset for training

'''

# check missing data for any row any column
# print(data.isnull().values.any())
# print(data.size)
# print(data.shape)
# print(data.dtypes)
# print(data.salary.unique())



# change value strint to number
# salary = {'high': 20000, 'low': 10000,'medium': 15000
# data.salary = [salary[item] for item in data.salary]
# print(data.salary)


clenup_data = {
    'salary' :{
        'low': 1,
        'medium' : 2,
        'high': 3
 
    }
}

data.replace(clenup_data, inplace=True)
# print(data)

# step 4 get dummies for deprnment

dummies = pd.get_dummies(data.Department)
# print(dummies)

# step 5 marge dumis column with original data
marge = pd.concat([data, dummies], axis = 'columns')
# print(marge)

# step 6 dorpe unnecessary data
final_data = marge.drop('Department', axis = 'columns')
# print(final_data.columns)

# step 7 show model
# plt.scatter(x = final_data.average_montly_hours, y = final_data.left)
# plt.show()

# step 8 split data
X = final_data.drop('left', axis = 'columns')
y = final_data.left
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


model = LogisticRegression()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
# print('accuracy', accuracy)
# print(list(X.columns))

result = model.predict([[0.42,0.53,2,142,1,0,1,0,1, 1, 0, 0, 0, 0, 0, 0, 0, 0]])
print(result)

