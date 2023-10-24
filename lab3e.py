'''
Name: Ronald Capili
Student ID: 152344222
Description: Math Quiz Version 2.0
'''

from random import randint

NUMBER_OF_QUESTIONS = 0 #Initialize number of questions to 0
correct_answers = 0     #Initialize # of correct answers to 0
user_num = 0            #Define a starting value for user input
user_input = 0          #Initialize user input to 0

while user_input != 'q':          #Checking if user quit
    num1 = randint(1,99)        #Initialize 1st random number
    num2 = randint(1,99)        #initialize 2nd random number
    while user_num != num1 + num2:            #Repeat loop while user input is != correct answer
        user_input = input("Enter the answer to " + str(num1) + " + " + str(num2) + ", or press 's' to skip or 'q' to quit: ")       #Ask math question
        if user_input == 's':           #If user inputs 's', skip question using break, increment number of questions
            NUMBER_OF_QUESTIONS += 1
            print ("Question skipped. 0 points awarded.")
            break
        elif user_input == 'q':         #If user inputs 'q', quit game, no increment to number of questions
            break
        else:
            num1 = int(num1)
            num2 = int(num2)
            user_num = int(user_input)  #Else, convert user input to int and check if answer is correct
        if user_num == num1 + num2:     #If user input is correct, increment correct answers and number of questions
            correct_answers += 1
            NUMBER_OF_QUESTIONS += 1
            print("Correct! You have been awarded 1 point!")
            print("Next question...")
        else:
            print("Incorrect. Try again.")
if NUMBER_OF_QUESTIONS == 0:
    grade = 00.0
else:
    grade = (correct_answers / NUMBER_OF_QUESTIONS) * 100.00
print("Quiz over. You scored %0.1f" % grade + "%.")   #Display grade in percentage