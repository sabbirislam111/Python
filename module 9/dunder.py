class Student:
    def __init__(self, neme, age, taka):
        self.neme = neme
        self.age = age
        self.taka = taka

    def __add__(self, other):
        return self.taka + other.taka

    def __call__(self):
        print(f"this is {self.neme} with age {self.age} have taka {self.taka}")

    def __lt__(self, other):
        return self.taka < other.taka


student_1 = Student("salman", 34, 5006)
student_2 = Student("limon", 25, 4589)
student_3 = Student("pankaj", 29, 789)


print(student_1 < student_3)


