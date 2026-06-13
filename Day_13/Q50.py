# Sum and average of array elements
n=int(input("Enter number of elements:"))
arr=[int(input(f"Enter element{i+1}:"))for i in range(n)]

total=sum(arr)
average=total/n
print("Array:",arr)
print("Sum:",total)
print("Average:",average)
