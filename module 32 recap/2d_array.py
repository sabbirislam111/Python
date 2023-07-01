# list = [[j for j in range(4)] for i in range(4)]
# print(list)

# r, c = (5,5)
# list = [[0]*r]*c
# print(list)


list = [[0 for i in range(4)]  for i in range(4)]
list[0][1] = 4
print(list)