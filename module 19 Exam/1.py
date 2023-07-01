def my_function(x):
  return x[::-1]
a = input("Enter your string :")
b = my_function(a)
if a == b: print('palindrome')
else: print('not a palindrome')

