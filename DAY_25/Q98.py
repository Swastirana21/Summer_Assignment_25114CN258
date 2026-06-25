# Find common characters in strings 
def common_characters(s1,s2):
    result=[]
    for char in s1:
        if char in s2 and char not in result:
            result.append(char)
    return result
s1="hello"
s2="world"
print(common_characters(s1,s2))
