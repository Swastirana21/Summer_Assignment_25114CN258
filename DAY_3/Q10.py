# Prime numbers in a range 

start=int(input("Enter a starting number:"))
end=int(input("Enter ending numbers:"))

for num in range(start,end+1):
    if num>1:
        for i in range(2,num):
            if num % i==0:
                break
        else:
            print(num,end=" ")