# Binary search 
def binary_search(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[2,5,8,12,16,23,38,45]
target=23
print("Binary search index of:",target,":",binary_search(arr,target))
