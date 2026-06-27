# Employee management system 
employees=[]
def add_employee(name,emp_id,department):
    employee={"name":name,"emp_id":emp_id,"department":department}
    employees.append(employee)
def display_employees():
    print("---Employee Records---")
    for e in employees:
        print("ID:",e["emp_id"],"| Name:",e["name"],"| Department:",e["department"])
name=input("Enter employee name:")
emp_id=int(input("Enter employee id:"))
department=input("Enter department:")
add_employee(name,emp_id,department)
display_employees()
