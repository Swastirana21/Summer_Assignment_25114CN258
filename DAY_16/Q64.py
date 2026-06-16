# Remove duplicated from array 
def remove_duplicates(arr):
    return list(dict.fromkeys(arr))

arr=[1,2,2,3,4,4,5]
print("After removing duplicate:",remove_duplicates(arr))
