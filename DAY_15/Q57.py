# Reverse: print array elements in reverse order
n=int(input("enter the number of elements:"))
arr=[int(input(f"enter elements{i+1}:"))for i in range(n)]

reversed_arr=arr[::-1]

print("Original array:",arr)
print("Reversed array:",reversed_arr)
