# modify class attributes
class Student:
    def __init__(self,stud_name,stud_marks):
        self.name = stud_name
        self.marks = stud_marks
        #self.new_stud_marks = new_stud_marks

    def changemarks(self, new_stud_marks):
        self.marks = new_stud_marks
        return Student.dispmarks(self)

    def dispmarks(self):
        return [self.name, self.marks]

first_stud = Student('Dan',55)
print(first_stud.dispmarks())
print(first_stud.changemarks(66))
