# Find maximum frequency element
def max_frequency_element(arr):
    freq={}
    for x in arr:
        freq[x]=freq.get(x,0)+1
        return max(freq,key=freq.get)
n=int(input("Enter number of elements:"))
arr=arr=[int(input(f"Enter elements{i+1}:"))for i in range(n)]
print("max frequency element:",max_frequency_element(arr))
