# Right rotation
n=int(input("Enter number of elements:"))
arr=[int(input(f"Enter elements{i+1}:"))for i in range(n)]
k=int(input("Enter number of positions to rotate right:"))

k=k%n
rotated=arr[-k:]+arr[:-k]

print("Original array:",arr)
print(f"array after right rotation by{k}:",rotated)
