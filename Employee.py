class Employee:
    def __init__(self,emp_id,emp_name,emp_hourly_wage):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.emp_hourly_wage=emp_hourly_wage
    def details(self):
        print("--------------------------")
        print("Id : ", self.emp_id)
        print("Name : ", self.emp_name)
        print("Hourly wage : ", self.emp_hourly_wage,"$")
        print("--------------------------------")
    #employes are saved into a dict of employee with the emp_id as the key and the information of the employee is saved as the value
employees = {}
def create_employee(emp_id,emp_name,emp_hourly_wage):
    #check if the Employee is already created
    #make sure it is not created before
    #if it is created just say the employee is already existing.
    if emp_id not in employees:
        new_employee= Employee(emp_id,emp_name,emp_hourly_wage)
        employees[emp_id]=new_employee
        print("Saved",emp_name,"as a new employee")
    else:
        print("Employee",emp_id,"is already existing")
def show_employees():
    for emp_id in employees:
        employee=employees[emp_id]
        employee.details()



def update_employee(emp_id,new_name,new_hourly_wage=0):
    if emp_id in employees:
        employee=employees[emp_id]
        if new_name and new_hourly_wage:
            employee.emp_name=new_name
            employee.emp_hourly_wage=new_hourly_wage
            print("employee with",emp_id,"is updated")
        else:
            print("inavlid arguments name and hourly wages has to be mentioned")
    else:
        print("employee with",emp_id,"does not exist")


def delete_employee(emp_id):
    if emp_id in employees:
        del employees[emp_id]
        print("Deleted successfully the employee",emp_id,"")
    else:
        print("Employee id:",emp_id,"is not found in the registry")




#days 25 per each dat 8hrs hourl wages are given.

def emp_salary(emp_id):
    if emp_id in employees:
        employee=employees[emp_id]
        salary=(25 * 8) * employee.emp_hourly_wage
        return salary
    
    else:
        raise Exception("not found")






create_employee("Emp1","Renuka",500)
create_employee("Emp2","renu ",400)
create_employee("Emp3","valli",600)
update_employee("Emp2","renu",420)
delete_employee("Emp3")
print(emp_salary("Emp2"))
show_employees()