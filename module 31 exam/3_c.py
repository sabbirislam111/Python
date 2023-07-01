
def getResult(A, B):
	Sum = A ^ B
	Carry = A & B
	print("Sum ", Sum)
	print("Carry", Carry)
    

while True:
    x, y = [int(x) for x in input("Enter two values: ").split()]
    ans = getResult(x, y)

 
 

