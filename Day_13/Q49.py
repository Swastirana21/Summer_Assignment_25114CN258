# Input and display array elementsn
n=int(input("Enter number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input(f"enter element{i+1}:")))

print("Array:",arr)
