
inp = "x3b4U5i2"
ans = ""
for i in range(0, len(inp), 2):
    for j in range(0, int(inp[i+1])):
      ans += inp[i]
res = ''.join(sorted(ans, key=str.lower))
print(res)

