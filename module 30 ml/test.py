
def getSod(x):

    someofDigits = 0
    while(x):
        last_digit = x%10
        someofDigits+=last_digit
        x/=10
        # print(int(someofDigits))
    return int(someofDigits)

def isValid(x, s):
    sodx = getSod(x)
    valid = bool((x - sodx) >= s)
    return valid


n = 10
s = 9

lo = 0
hi = n
ans = -1

while(lo <= hi):
    mid = (lo + hi) / 2
    if isValid(mid, s):
        ans = mid
        hi = mid -1
    else:
        lo = mid + 1
if ans == -1:
    print(0)
else:
    print(n - ans +1)










# a = getSod(10)
# print(a)
