# Find pair with given sum 
def find_pair_with_sum(arr,target):
    seen=set()
    for num in arr:
        complement=target-num
        if complement in seen:
            return (complement,num)
        seen.add(num)
    return None
arr=[1,4,7,2,9,3]
target=11
print("pair with sum",target,";",find_pair_with_sum(arr,target))

