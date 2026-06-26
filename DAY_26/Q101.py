# Number guessing game 
import random
def number_guessing_game():
    number=random.randint(1,10)
    guess=int(input("Guess a number between 1 and 10:"))
    if guess==number:
        print("Correct! You guessed it!")
    elif guess<number:
        print("Too low! Try again")
    else:
        print("Too high! Try again")
    print("The number was:",number)

number_guessing_game()

       