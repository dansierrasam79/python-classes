# display Student attributes

class Student:
    def __init__(self, stud_name, stud_id,stud_major):
        self.name = stud_name
        self.id = stud_id
        self.major = stud_major

    def disp_student_rec(self):
        return [self.name, self.id, self.major]

init_stud_obj = Student("Daniel",12200,250000)
print(init_stud_obj.disp_student_rec())
