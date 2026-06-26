# Voting eligibility system 
def check_voting_eligibility(age):
    if age>=18:
        print("eligible to vote")
    else:
        print("Not eligible to vote")
age=int(input("Enter your age:"))
check_voting_eligibility(age)

