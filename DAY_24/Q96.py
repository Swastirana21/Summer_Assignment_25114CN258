# Remove duplicate characters 
def remove_duplicate_chars(s):
    result=""
    for char in s:
        if char not in result:
            result+=char
    return result
s="programming"
print(remove_duplicate_chars(s))
