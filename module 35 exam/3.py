"""
types of scope in python
1. Local Scope
2. Global Scope
3. NonLocal or Enclosing Scope
4. Built-in Scope

"""

"""  Local Scope  """

# num=0 
# def demo():#Local Scope
#     print(num) # print befor declarations
#     num=1 
#     print("The Number is:",num)
# demo()

""""  Global Scope   """

# def demo(): # Local Scope 
#     # print(Str) 
#     Str = "You are smart"
#     print(Str) 
# # Global scope 
# Str = "You are Clever" 
# demo() 
# print(Str)

""""  NonLocal or Enclosing Scope   """

# def func_outer():
#     x = "local"
#     def func_inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#     print("outer:", x)  
#     func_inner() # Enclosing Scope   
#     print("outer:", x)
# func_outer()


""""    Built-in Scope  """


# # Built-in Scope 
# from math import pi 
# # pi = 'Not defined in global pi'
# def func_outer(): 
#     # pi = 'Not defined in outer pi' 
#     def inner(): 
#         # pi = 'not defined in inner pi' 
#         print(pi) 
#     inner() 
# func_outer()

 