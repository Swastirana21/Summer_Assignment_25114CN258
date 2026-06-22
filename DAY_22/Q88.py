# Remove spaces from string 
def remove_spaces(s):
    result=""
    for char in s:
        if char !=" ":
            result+=char
    return result
s="Hello world pyhton"
print(remove_spaces(s))

