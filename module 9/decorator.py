
import math

def timer(func):
    def inner(n, **kwargs):
        print("Timer started")
        func(n, **kwargs)
        print("Timer finished")
    return inner



@timer
def get_function(n, **kwargs):
    fact = math.factorial(n, **kwargs)
    print(f"{n} factorial is {fact}")

get_function(n = 8)
