import re
par = "I am sure that the shells are seashore shells. So if she sells seashells on the seashore, The shells that she sells are seashells, I am sure She sells seashells on the seashore;"

for i in re.split(r'[,.]', par):
    print(i.center(500))


   




