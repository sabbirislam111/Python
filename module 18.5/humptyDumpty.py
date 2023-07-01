
A = "HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandallt heKingsmenCouldntputHumptyDumptyinhisplaceagain. "

# a, b, c, d = input("Enter two values: ").split()

a = 22
b = 27
c = 97
d = 102 

result = ""

for i in range(a, b+1) :
    result += A[i]
    
    
result+= ' '
for i in range(c+1, d+2) :
    result += A[i]
    
print(result)
