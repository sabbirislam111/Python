import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv('write.csv')
plt.scatter(data['version'], data['price'])
plt.show()