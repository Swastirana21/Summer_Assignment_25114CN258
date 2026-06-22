# Find string length without strlen()/len() 
def string_length(s):
    count=0
    for _ in s:
        count+=1
    return count
s="Hello,World!"
print(f"String length:",string_length(s))
