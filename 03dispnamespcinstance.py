#display namespace of instance

class Employee:
    def __init__(self, emp_name, emp_id, salary):
        self.empname = emp_name
        self.empid = emp_id
        self.salary = salary
    def display_emp_info(self):
        print("Employee Name:", self.empname)
        print("Employee ID:", self.empid)
        print("Employee Salary:", self.salary)

first_emp = Employee("Daniel Chakraborty",1000,250000)
print(first_emp.__dict__)
