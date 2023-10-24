'''
Name: Ronald Capili
Student ID: 152344222
Description: Word Game
'''

from random import randint  

animals = ['snake','hamster','scorpion','beaver','mosquito','camel','vulture','horse','python','capybara']      #Initialize contents of list
secret=animals[randint(0,len(animals)-1)]           #Select random item from animals list
print("I'm thinking of an animal. Can you guess what it is?")                       #Welcome message

userinput=0                                 #Initialize to zero to make a loop until user enters "Enter"
while userinput != "":                      #Loop until user enters "Enter"
    userinput = input("Enter a letter or a guess. Press enter to quit: ")         #Ask input
    if userinput == "":                                                                 #Quit if user hits "Enter" only
        break
    elif len(userinput) > 1:                            #If input is more than 1 character
        if userinput == secret:                         #Check if it matches the secret word
            print("You win!")
            userinput = ""                              #Set userinput to "Enter" to break loop
        else:
            print("Sorry, that's not it.")
    else:                                               #If input is just 1 character
        if userinput in secret:                         #Check if character is within secret word
            print("Yes, my word contains that letter.")
        else:
            print("Sorry, my word doesn't contain that letter.")