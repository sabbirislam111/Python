# Two Lists
list1 = ['BMW', 'Toyota', 'audi', 'Tesla', 'Hyundai']
list2 = [2, 5, 1, 4, 3]

print("List1 = ",list1)
print(sorted(zip(list2, list1)))

# Sorting the List1 based on List2
res = [val for (_, val) in sorted(zip(list2, list1), key=lambda x: x[0])]
print("Sorted List = ",res)