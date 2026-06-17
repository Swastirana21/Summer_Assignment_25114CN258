# Union of arrays 
def union_of_arrays(arr1,arr2):
    return list(set(arr1) | set(arr2))
arr1=[1,2,3,4]
arr2=[3,4,5,6]
print("Union:",sorted(union_of_arrays(arr1,arr2)))
