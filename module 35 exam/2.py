

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

key = [1, 2, 3, 4, 5]
lst = []


for i in range(1, 5):
    for j in range(1, 6):
        if i != j:
            lst.append(j)

a = to_matrix(lst, 4)


user_Dict = { X:Y for (X,Y) in zip(key, a)}  
print(dict(user_Dict)) 