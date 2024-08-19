#find instanceof and subclassof
class Student:
    def __init__(self,stud_id,stud_name):
        pass

class Marks:
    def __init__(self,cs,maths):
        pass

first_stud = Student(12055,'Dan')
first_marks = Marks('CS','Maths')

print(isinstance(first_stud,Student))
print(isinstance(first_marks,Marks))
print(issubclass(Marks, object))
print(issubclass(Student, object))
