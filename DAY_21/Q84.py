# Convert lowercase to uppercase
def to_uppercase(s):
    result=" "
    for char in s:
        if 'a'<=char <='z':
            result+=chr(ord(char)-32)
        else:
            result+=char
    return result
s="hello world"
print("Upercase:",to_uppercase(s))
