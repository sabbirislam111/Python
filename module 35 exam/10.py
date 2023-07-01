# Single Inheritance: 

class A:
    def __init__(self):
        pass

class B:
    def __init__(self):
        pass

class C:
    def __init__(self):
        pass


# Multiple Inheritance: 

class  A:
    def __init__(self):
        pass
class B:
    def __init__(self):
        pass

class C(A, B):
    def __init__(self):
        pass

# Multilevel Inheritance

class  A:
    def __init__(self):
        pass
class B(A):
    def __init__(self):
        pass

class C(B):
    def __init__(self):
        pass