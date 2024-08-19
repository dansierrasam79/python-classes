# add and delete class attributes
class Student:
    def __init__(self, stud_name, stud_id):
        self.name = stud_name
        self.id = stud_id
        self.clss = None
        
    def disp_attrs(self):
        if not self.clss: 
            return [self.name, self.id]
        elif not self.name:
            return [self.id, self.clss]
        else:
            return [self.name, self.id,self.clss]

    def add_attr(self,stud_class):
        self.clss = stud_class
        return Student.disp_attrs(self)

    def del_attr(self,stud_name):
        if self.name == stud_name:
            self.name = None
        return Student.disp_attrs(self)
    

stud_object = Student('Dan',12500)

print(stud_object.disp_attrs())

print(stud_object.add_attr("Computer Science"))

print(stud_object.del_attr('Dan'))
