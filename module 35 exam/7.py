lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lst2 = []
for i in lst:
    if i % 3 == 0:
        lst2.append(i)
print(lst2)