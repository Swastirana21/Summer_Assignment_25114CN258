# Linear search: search element one by one from start
n=int(input("Enter number of elements:"))
arr=[int(input(f"Enter element{i+1:}:"))for i in range(n)]

key=int(input("Enter elementto  search:"))
found=False
for i in range(n):
    if arr[i]==key:
        print(f"Element {key} found at index {i}(position {i+1})")
        found=True
        break
if not found:
    print(f"Element {key} not found in array")


