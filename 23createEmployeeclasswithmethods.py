# Employee class with methods
class Employee:
    def __init__(self,emp_name,emp_id,emp_salary,emp_department):
        self.empid = emp_id
        self.empname = emp_name
        self.empsal = emp_salary,
        self.empdep = emp_department

    def print_emp_deets(self,name):
        try:
            if name == self.empname:
                print("Employee Name: ", self.empname)
                print("Employee ID: ", self.empid)
                print("Salary: ",self.empsal)
                print("Employee Department: ", self.empdep)
        except:
            print("No such employee name exists")

    def emp_assign_department(self,name,new_dept):
        if name == self.empname:
            self.empdep = new_dept
        return Employee.print_emp_deets(self,name)

    def calc_emp_sal(self,hours_worked):
        if hours_worked > 50:
            overtime_amnt = (hours_worked - 50)*(self.empsal[0]/50)
            print("Employee Salary: ", self.empsal[0] + overtime_amnt)
        else:
            print("Employee Salary: ", self.empsal[0])
        

if __name__ == "__main__":
    import sys
    emp_list = [{"name":"Adams", "empid":"E7876", "salary":50000, "dept":"ACCOUNTING"}, {"name":"JONES", "empid":"E7499", "salary":45000, "dept":"RESEARCH"},
                {"name":"Martin", "empid":"E7900", "salary":50000, "dept":"SALES"},
                {"name":"Smith", "empid":"E7698", "salary":55000, "dept":"OPERATIONS"}]
    
    # add all employee objects using a list of dicts instead of keying it in
    first_emp_obj = Employee(emp_list[0].get("name"),emp_list[0].get("empid"),emp_list[0].get("salary"),emp_list[0].get("dept"))
    sec_emp_obj = Employee(emp_list[1].get("name"),emp_list[1].get("empid"),emp_list[1].get("salary"),emp_list[1].get("dept"))        
    thrd_emp_obj = Employee(emp_list[2].get("name"),emp_list[2].get("empid"),emp_list[2].get("salary"),emp_list[2].get("dept"))
    frth_emp_obj = Employee(emp_list[3].get("name"),emp_list[3].get("empid"),emp_list[3].get("salary"),emp_list[3].get("dept"))

    all_objects = [first_emp_obj,sec_emp_obj,thrd_emp_obj,frth_emp_obj]

    while True:
        print("Main Menu")
        print("1. Access Employee Information")
        print("2. Change Employee Department")
        print("3. Compute Employee Salary")
        print("4. Exit")
        choice = input("Enter a choice: ")

        if choice == "1":
            # access an employee's information
            name = input("Enter a name: ")
            for emp_obj in all_objects:
                emp_obj.print_emp_deets(name)
        elif choice == "2":
            # change employee department
            name = input("Enter a name: ")
            new_dept = input("Enter the new department name: ")
            for emp_obj in all_objects:
                dept_change_complete = emp_obj.emp_assign_department(name,new_dept)
            if dept_change_complete:
                print(dept_change_complete)
        elif choice == "3":
            # compute employee salary and return as a list
            hours_worked = [80,92,34,60]
            idx = 0
            for emp_obj in all_objects:
                emp_obj.calc_emp_sal(hours_worked[idx])
                idx += 1
        elif choice == "4":
            print("Bye Bye Birdie")
            sys.exit(0)
    
    
