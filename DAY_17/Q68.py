# Find common elements (among three arrays) 
def find_common_elements(arr1,arr2,arr3):
    return list(set(arr1)&set(arr2)&set(arr3))
arr1=[1,2,3,4]
arr2=[2,3,4,5]
arr3=[3,4,5,6]
print("Common elements:",sorted(find_common_elements(arr1,arr2,arr3)))
