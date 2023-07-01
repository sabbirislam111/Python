
class School:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello form school!")

class  Teacher:
    def __init__(self, name):
        self.teacherName = name

    def say_hello(self):
        print("Hello form Teacher!")



class Student:
    def __init__(self, name, obj):
        self.studentName = name
        obj.say_hello()
    
    

school = School("SN high school")
ruman = Teacher("Riman mia")


student = Student("sabbir", ruman)





