class School:
    def __init__(self,name):
        self.schoolName = name
    def __repr__(self) -> str:
        return f"({self.schoolName})"

class Teacher:
    def __init__(self,name):
        self.teacherlName = name
    def __repr__(self) -> str:
        return f"({self.teacherlName})"

class Student(Teacher, School):
    def __init__(self,name, teacherlName, schoolName):
        self.studentName = name
        Teacher.__init__(self,teacherlName)
        School.__init__(self,schoolName)
        
    def __repr__(self) -> str:
        return f"({self.studentName})"

sabbir = Student("sabbir", "Delower", "SN high school")
print(sabbir.teacherlName)

