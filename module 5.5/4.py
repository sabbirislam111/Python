list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

ans = list(zip(list1, list(reversed(list2))))
print(ans)
