# Function for palindrome
def palindrome(n):
    return str(n)==str(n)[::-1]

n=input("Enter value:")
if palindrome(n):
    print("Palindrome")
else:
    print("Not palindrome")
    
