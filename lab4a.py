'''
Name: Ronald Capili
Student ID: 152344222
Description: Guess a Number Game - Version 3.0 - with exception handling
'''
from random import randint


secret = randint(1, 10)  #Initialize random secret number value
user_guess = 0  #Initialize user_guess to zero

while user_guess != secret:     #While Loop to keep asking user for a guess until user get's it right
    user_guess = input("Enter a number between 1 and 10: ")             #Ask input
    if user_guess.isnumeric() and 0 < int(user_guess) < 11:             #Check for wrong input
        user_guess = int(user_guess)
        if user_guess == secret:                                                #Check if guess is correct
            print("Correct! You win.")                                          #Print successful guess
        else:
            print("Sorry, try again.")                                      #Print that guess is wrong
    else:
        print("Error: not a number or out of bounds.")                  #If user_guess is not number, or less than 0, or greater than 10, print input error