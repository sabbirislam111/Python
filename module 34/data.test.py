
import pandas as pd
import math
import json
import matplotlib.pyplot as plt

data = pd.read_csv('Salary_Data.csv')
head_data = data.columns.values

x = data[head_data[0]]
y = data[head_data[1]]
x = x.truncate(20, 29)
y = y.truncate(20, 29)

# pradicted data y = m*x_mean _ c
with open('data_dict.txt','r') as file:
    datas = file.read()
    converted_data = json.loads(datas)
m = converted_data['m']
c = converted_data['c']

y_pradict_list = []
r_upar = 0
r_lower = 0
for indx in range(len(x)):
    y_pradict = m*x[indx] + c
    y_pradict_list.append(y_pradict)




# plt.scatter(x, y, color= 'r')
# plt.plot(x, y_pradict_list, color= 'g')
# plt.show()