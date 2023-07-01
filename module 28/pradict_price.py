import pandas
from sklearn.linear_model import LinearRegression
pandas.DataFrame()

data = pandas.read_csv('write.csv') 
model = LinearRegression()
model.fit(data[['version']], data[['price']])
pradict_peice = model.predict([[20]])
print(pradict_peice)