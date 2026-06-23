# Find first repeating character 
def first_repeating(s):
    seen=[]
    for char in s:
        if char in seen:
            return char
        seen.append(char)
    return "No repeating charcter found"
s="abcdeab"
print(first_repeating(s))
