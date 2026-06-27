# Salary management system 
def calculate_salary(basic):
    hra=basic*0.20
    da=basic*0.10
    tax=basic*0.05
    gross=basic+hra+da
    net=gross=tax
    print("Basic salary:",basic)
    print("HRA(20%):",hra)
    print("DA (10%):",da)
    print("Tax (5%):",tax)
    print("Gross salary:",gross)
    print("Net salary:",net)

basic=int(input("Enter basic salary:"))
calculate_salary(basic)
