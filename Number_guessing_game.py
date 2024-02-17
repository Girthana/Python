"""
Program: Building Number Guessing Game
Input: Range for Number guessing (Ex: 1 to 100)
Number of guesses: log_2(Upper bound-lower bound+1)
"""
import random
import math
low_bd=int(input("Enter the lower bound for guessing the number:"))
upp_bd=int(input("Enter the upper bound for guessing the number:"))

rand_no=random.randint(low_bd,upp_bd)
print("Random number is ",rand_no)

no_guess=round(math.log2(upp_bd-low_bd+1))
print("You have ", no_guess," chances for guessing the number");
count =0;
while(count<no_guess):
    count=count+1
    guess=int(input ("Guess a number"))
    #print ("The number guessed is ",guess)
    if(guess == rand_no):
        print("You have guessed the number correctly")
    elif (guess < rand_no):
        print("Your Guess is small...")
    else:
        print("Your guess is high...")
if(count==no_guess):
    print("Better luck next time")
    