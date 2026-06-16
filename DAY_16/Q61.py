# Find missing number in array
def find_missing_number(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            return i
arr=[1,2,4,5,6]
n=6
print("Input:",arr)
print("Output:missing number=",find_missing_number(arr,n))