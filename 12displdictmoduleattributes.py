# display __dict__ and __module__ attributes
class Student:
    def __init__(self, stud_name, stud_id, stud_maj):
        self.name = stud_name
        self.id = stud_id
        self.major = stud_maj

    def disp_stud_info(self):
        print(self.name, self.id, self.major)

stud_obj = Student('Dan', 12055,'Computer Science')

print(Student.__dict__.keys())
print(Student.__module__)
