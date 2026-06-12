# Function for armstrong number

def armstrong(n):
    s=sum(int(d)**len(str(n))for d in str(n))
    return s==n
n=int(input("Enter number:"))
if armstrong(n):
    print("armstrong number")
else:
    print("not an armstong number")

