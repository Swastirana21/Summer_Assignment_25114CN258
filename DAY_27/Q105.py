# Student record management system 
students=[]
def add_student(name,roll,marks):
    student={"name":name,"roll":roll,"marks":marks}
    students.append(student)
def display_students():
    print("---student records---")
    for s in students:
        print("Roll:",s["roll"],"| Name:",s["name"],"| Marks:",s["marks"])
name=input("Enter student name:")
roll=int(input("enter roll number:"))
marks=int(input("Enter marks:"))
add_student(name,roll,marks)
display_students()

