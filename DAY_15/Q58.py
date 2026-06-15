# Left rotations:shift all elements to the left by k positions
n=int(input("Enter number of elements:"))
arr=[int(input(f"Enter elements{i+1}:"))for i in range(n)]

k=int(input("ENter number of positions to rotate left:"))
k=k%n
rotated=arr[k:]+arr[k:]

print("Original array:",arr)
print(f"Array after left rotation by {k}:",rotated)
