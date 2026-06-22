# Check palindrome string 
def check_palindrome(s):
    reversed_s=""
    for char in s:
        reversed_s=char+reversed_s
    if s==reversed_s:
        return"Yes,it is a palindrome"
    else:
        return "No,it is not a palindrome"
s="madam"
print(check_palindrome(s))


    