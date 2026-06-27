# Marksheet generation system 
def marksheet():
    name=input("ENter student name:")
    roll=input("Enter roll number:")
    m1=int(input("Enter marks in subject 1:"))
    m2=int(input("Enter marks in subject 2:"))
    m3=int(input("Enter marks in sybject 3:"))
    total=m1+m2+m3
    average=total/3
    if average >=90:
        grade="A"
    elif average>=75:
        grade="B"
    elif average>=60:
        grade="C"
    elif average>=50:
        grade="D"
    else:
        grade="F"
    if average>=50:
        result="Pass"
    else:
        result="Fail"

    print("----Marksheet----")
    print("Name:",name)
    print("roll no :",roll)
    print("Subject 1:",m1)
    print("Subject 2:",m2)
    print("Subject 3:",m3)
    print("Total:",total)
    print("Average:",average)
    print("Grade:",grade)
    print("Result:",result)
    print("-------------------")

marksheet()
