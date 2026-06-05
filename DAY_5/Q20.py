# To find largest prime factor 
 
n=int(input("Enter a number:"))
largest=1

for i in range(2,n+1):
    if n%i==0:
        prime=True

        for j in range(2,i):
            if i%j==0:
                prime=False
                break
                 
            
        if prime:
            largest=i
print("Largest prime factor=",largest)
