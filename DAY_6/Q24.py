# To find x^n 
x=int(input("Enter base:"))
n=int(input("Enter power:"))

result=1

for i in range (n):
    result*=x

print("Result=",result)