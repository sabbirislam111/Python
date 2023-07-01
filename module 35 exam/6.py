
n = int(input('Enter the size : '))
lst = []

for i in range(1,n+1):
    lst.append(i)

for indx in range(len(lst)):
    if indx == 0:
         result = ' '.join(str(item) for item in lst)
         print(result)
    else:
        rsv = lst[indx-1]
        rsv2 = lst[indx]
        lst[indx] =  rsv
        lst[indx-1] =rsv2
        result = ' '.join(str(item) for item in lst)
        print(result)
        

