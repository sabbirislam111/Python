from threading import Thread

def f1():
    for i in range(5):
        print(f"f1 - {i}")
 
def f2():
    for i in range(5):
        print(f"f2 - {i}")
 
def f3():
    for i in range(5):
        print(f"f3 - {i}")
       
def f4():
    for i in range(5):
        print(f"f4 - {i}")

a1 = Thread(target=f1)
a2 = Thread(target=f2)
a3 = Thread(target=f3)
a4 = Thread(target=f4)

a1.start()
a2.start()
a3.start()
a4.start()

a1.join()
a2.join()
a3.join()
a4.join()

