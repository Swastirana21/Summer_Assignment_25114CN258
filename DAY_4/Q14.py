# To find nth fibonacci series 

n= int(input("Enter n:"))
a,b=0,1
for i in range(n-1):
    a,b=b,a+b
print("Nth fibonacci term= ",a)
