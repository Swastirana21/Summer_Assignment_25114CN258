# To check armstrong number
 
n= int(input("Enter a number:"))

sum=0
temp=n
digits=len(str(n))

while temp>0:
    digit=temp % 10
    sum+= digit**digits
    temp//=10

if sum==n:
    print("Armstrong number")
else:
    print("Not an armstrong number")
    