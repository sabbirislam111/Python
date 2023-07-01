class Student:
  
    def __init__(self, name, mark, id):
            self.name = name
            self.mark = mark
            self.id = id
          
i = 1
student_1 = Student("sabbir", 20, 234+i)
i += 1
student_2 = Student("salman", 26, 234+i)
i += 1

print(student_1.name, student_1.mark, student_1.id)
print(student_2.name, student_2.mark, student_2.id)
        
    
