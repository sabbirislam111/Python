class student:
    
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class corse:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher

class teacher:
    def __init__(self, name, course):
        self.name = name
        self.course = course

class school:
    def __init__(self, name, teachers, students, courses):
        self.name = name
        self.teachers = teachers
        self.students = students
        self.courses = courses
    def get_students(self):
        for student in self.students:
            print(student.name)
    

school_mane = "SN High School"
ds_course = corse("Dara structure course", "Kanay lal pathak")
teacher_1 = teacher("Kanay lal pathak", ds_course)
algo_course = corse("Algorith course", "Deloer Islam")
teacher_2 = teacher("Deloer Islam", algo_course)

student_1 = student("Sabbir", 26, 50)
student_2 = student("Dipika", 46, 55)
student_3 = student("Latas", 35, 78)


teachers = [teacher_1, teacher_2]
courses = [ds_course, algo_course]
students = [student_1, student_2, student_3]

my_school = school(school_mane, teachers, students, courses)

my_school.get_students()

