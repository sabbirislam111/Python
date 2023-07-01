# MRC calculate

import pandas as pd
import math
import json

def mean_func(data):
    sum = 0
    for i in data:
        sum += i
    mean = sum / len(data)
    return mean

data = pd.read_csv('Salary_Data.csv')
head_data = data.columns.values

x = data[head_data[0]]
y = data[head_data[1]]
x = x.truncate(0, 19)
y = y.truncate(0, 19)

x_mean = mean_func(x)
y_mean = mean_func(y)


up = 0
down = 0
for indx in range(len(data)):
    up+= (x[indx] - y_mean) * (y[indx] - y_mean)
    down+= math.pow(x[indx] - x_mean, 2)

m = up/down
c = (y_mean) - (m*x_mean)
train_data = {}
train_data['m'] = m
train_data['c'] = c
# train_data['y_mean'] = y_mean
with open('data_dict.txt', 'w') as file:
    file.write(json.dumps(train_data))
