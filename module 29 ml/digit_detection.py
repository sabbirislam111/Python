from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt

digit = load_digits()
# print(dir(digit))

# plt.gray()
# plt.matshow(digit.images[0])
# plt.show()

x = digit.data
y = digit.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

print(x_train)

# print(x_train.shape)
# print(x_test.shape)

model = LogisticRegression()
model.fit(x_train, y_train)

# print('target value of the test', digit.target[1700])
# result = model.predict([digit.data[1700]])
# print('pradict data', result)


accrucy = model.score(x_test, y_test)
# print(accrucy)

y_pradicted = model.predict(x_test)
confusion = confusion_matrix(y_test, y_pradicted)
# print(confusion)
plot_confusion_matrix(model, x_test, y_test)
plt.show()
