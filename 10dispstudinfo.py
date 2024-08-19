# display student id, name or class

class Student:
    def __init__(self,stud_id,stud_name = None,stud_class = None):
        self.id = stud_id
        self.name = stud_name
        self.clss = stud_class

    def displaystudrec(self):
        student_rec = []
        student_rec.append(self.id)
        if self.name:
            student_rec.append(self.name)
        if self.clss:
            student_rec.append(self.clss)
        return student_rec

first_student_rec = Student(10555, stud_name = "Daniel")
print(first_student_rec.displaystudrec())
second_student_rec = Student(10212, stud_class = "Computer Science")
print(second_student_rec.displaystudrec())
