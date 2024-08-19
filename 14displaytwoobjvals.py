# display two object's values
class Student:
    def __init__(self, stud_name, stud_id, stud_class):
        self.name = stud_name
        self.id = stud_id
        self.clss = stud_class

    def disp_attrs(self):
        return [self.name,self.id,self.clss]

first_stud = Student('Dan',12055,"CS")
second_stud = Student('Mark',12056,'Business')
print(first_stud.disp_attrs())
print(second_stud.disp_attrs())
