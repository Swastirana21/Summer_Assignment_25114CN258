# Reverse a string 
def reverse_string(s):
    reversed_s=" "
    for char in s:
        reversed_s=char+reversed_s
    return reversed_s
s="Python"
print(f"Reversed string:",reverse_string(s))
