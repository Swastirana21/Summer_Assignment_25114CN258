# Bubble sort 
def bubble_sort(arr):
    arr=arr.copy()
    n=len(arr)
    for i in range (n-1):
        for j in range(n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[64,34,25,12,22,11,90]
print("Bubble sort:",bubble_sort(arr))
