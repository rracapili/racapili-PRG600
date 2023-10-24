'''
Name: Ronald Capili
Student ID: 152344222
Description: Math Quiz 
'''

NUMBER_OF_QUESTIONS = 4
correct_answers = 0

num = 0         #Define a starting value for user input
while num != 26:        #Hardcoded checking of the correct answer
    user_input = input("Enter the answer to 12 + 14, or press 's' to skip: ")       #Check if user wants to skip question
    if user_input == 's':
        print ("Question skipped. 0 points awarded.")
        break
    else:
        num = int(user_input)                                                       #Take user input as integer and check value
    if num != 26:                                                                   #If incorrect, ask question again
        print("Incorrect. Try again.")
    else:                                                                           #If correct, award a point
        correct_answers += 1
        print("Correct! You have been awarded 1 point!")
print("Next question...")                                                           #Go to next question

num = 0         #Define a starting value for user input
while num != 31:        #Hardcoded checking of the correct answer
    user_input = input("Enter the answer to 23 + 8, or press 's' to skip: ")       #Check if user wants to skip question
    if user_input == 's':
        print ("Question skipped. 0 points awarded.")
        break
    else:
        num = int(user_input)                                                       #Take user input as integer and check value
    if num != 31:                                                                   #If incorrect, ask question again
        print("Incorrect. Try again.")
    else:                                                                           #If correct, award a point
        correct_answers += 1
        print("Correct! You have been awarded 1 point!")
print("Next question...")                                                           #Go to next question

num = 0         #Define a starting value for user input
while num != 43:        #Hardcoded checking of the correct answer
    user_input = input("Enter the answer to 30 + 13, or press 's' to skip: ")       #Check if user wants to skip question
    if user_input == 's':
        print ("Question skipped. 0 points awarded.")
        break
    else:
        num = int(user_input)                                                       #Take user input as integer and check value
    if num != 43:                                                                   #If incorrect, ask question again
        print("Incorrect. Try again.")
    else:                                                                           #If correct, award a point
        correct_answers += 1
        print("Correct! You have been awarded 1 point!")
print("Next question...")                                                           #Go to next question

num = 0         #Define a starting value for user input
while num != 44:        #Hardcoded checking of the correct answer
    user_input = input("Enter the answer to 17 + 27, or press 's' to skip: ")       #Check if user wants to skip question
    if user_input == 's':
        print ("Question skipped. 0 points awarded.")
        break
    else:
        num = int(user_input)                                                       #Take user input as integer and check value
    if num != 44:                                                                   #If incorrect, ask question again
        print("Incorrect. Try again.")
    else:                                                                           #If correct, award a point
        correct_answers += 1
        print("Correct! You have been awarded 1 point!")

grade = (correct_answers / NUMBER_OF_QUESTIONS) * 100.00
print("You received a grade of %0.1f" % grade + "%.")   #Display grade in percentage