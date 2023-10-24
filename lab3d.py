'''
Name: Ronald Capili
Student ID: 152344222
Description: Guess a Number Game - Version 2.0
'''
from random import randint


secret = randint(1, 10)  #Initialize random secret number value
user_guess = 0  #Initialize user_guess to zero

while user_guess != secret:     #While Loop to keep asking user for a guess until user get's it right
    user_guess = int(input("Guess a number between 1 and 10: "))            #Ask input
    if user_guess == secret:                                                #Check if guess is correct
        print("Correct! You win.")                                          #Print successful guess
    else:
        print("Sorry, that's not it.")                                      #Print that guess is wrong