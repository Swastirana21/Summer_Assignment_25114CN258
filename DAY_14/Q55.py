# Second largest: largest element excluding the maximum
n=int(input("Enter the number of elements:"))
arr=[int(input(f"Enter the elements {i+1}:"))for i in range(n)]

unique=list(set(arr))
unique.sort()

if len(unique)<2:
    print("No second largest element exists")
else:
    print("Array:",arr)
    print("Second largest element:",unique[-2])
    