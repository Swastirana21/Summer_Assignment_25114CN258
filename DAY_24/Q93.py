# Check string rotation 
def check_rotation(s1,s2):
    if len(s1)!=len(s2):
        return "Not a rotation"
    combined=s1+s2
    if s2 in combined:
        return "Yes,it is a rotation"
    else:
        return "Not a rotation"
    
s1="abcde"
s2="cdeab"
print(check_rotation(s1,s2))
