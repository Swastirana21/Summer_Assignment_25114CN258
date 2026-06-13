# Find largest and smallest element in array
n=int(input("Enter number of eements:"))
arr=[int(input(f"Enter element{i+1}:"))for i in range(n)]

print("Array:",arr)
print("Largest element:",max(arr))
print("Smallest element:",min(arr))
