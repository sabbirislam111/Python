
from linecache import cache

from functools import cache


@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n-1) + fib(n-1)


for i in range(50):
    print(i, fib(i))