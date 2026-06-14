# Duplicate: elements that appear more than once
n=int(input("Enter the number of elements:"))
arr=[int(input(f"Enter the elements{i+1}:"))for i in range(n)]
duplicates=[]
for x in arr:
    if arr.count(x)>1 and x not in duplicates:
        duplicates.append(x)

print("Array:",arr)
if duplicates:
    print("Duplicate elements:",duplicates)
else:
    print("No duplicate found")
    