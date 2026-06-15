# Move all zeroes to the end while maintaining order of other elements
n=int(input("Enter number of elements:"))
arr=[int(input(f"Enter elemets{i+1}:"))for i in range(n)]

non_zeroes=[x for x in arr if x!=0]
zeroes=[x for x in arr if x==0]
result=non_zeroes+zeroes

print("Original array:",arr)
print("Array after moving zeroes to end",result)
