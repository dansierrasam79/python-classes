# add new class attr
class Student:
    def __init__(self,stud_name,stud_id):
        self.name = stud_name
        self.id = stud_id
        self.clss = None

    def add_attr(self,stud_class):
        self.clss = stud_class
        return Student.disp_attr(self)

    def disp_attr(self):
        if not self.clss:
            return [self.name,self.id]
        else:
            return [self.name,self.id,self.clss]

stud_obj = Student('Dan',12055)
print(stud_obj.disp_attr())
print(stud_obj.add_attr('Computer Science'))
