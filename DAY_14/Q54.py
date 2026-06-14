# Frequency: how many times an element appears in array

n=int(input("Enter number of elements:"))
arr=[int(input(f"enter elements {i+1}:"))for i in range(n)]
key=int(input("Enter element to find frequency:"))
frequency=arr.count(key)

print("Array:",arr)
print(f"frequency of {key}:",frequency)
