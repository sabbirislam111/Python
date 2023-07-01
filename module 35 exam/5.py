data=[{'a':5,'b':10},{'x':15,'y':20}]
for val in range(len(data)):
    for dt in data[val].items():
        print(f"Key:{dt[0]} Value:{dt[1]}")
