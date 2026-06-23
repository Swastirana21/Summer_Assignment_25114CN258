# Find maximum occuring character 
def max_occuring_char(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    max_char=""
    max_count=0
    for char in freq:
        if freq[char]>max_count:
            max_count=freq[char]
            max_char=char
    return max_char
s="hello world"
print(max_occuring_char(s))
