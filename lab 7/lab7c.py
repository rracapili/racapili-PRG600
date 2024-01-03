'''
Name: Ronald Capili
Student ID: 152344222
Description: Modifying A Dictionary
'''

from lab7b import print_meal_plan   #Import the print_meal_plan function from lab7b
menu = []   #Initialize menu list

template = {'breakfast': None, 'lunch': None, 'dinner': None}   #Initialize a template dictionary with values set to None. 


while True:     #Use loop to ask user if they want to input more to the menu
    
    add_day = input("Would you like to add a day? (y/n)")       #Ask user if they want to add a day

    
    if add_day.lower() == 'n':      #Stop adding days when user enters 'n'
        break    
    elif add_day.lower() == 'y':    #If user entered yes, create new template new_day.
        new_day = template.copy()
        for key in new_day:         #Iterate through the keys breakfast, lunch and dinner and ask user to enter a meal idea
            new_day[key] = input(f"Please enter what you would like to eat for {key}:")
        menu.append(new_day)    #Add new_day to menu list
    else:           #Check for invalid input if user enters anything other than 'y' or 'n'
        print("Error: Please enter 'y' or 'n'.")
day_num = int(input("Please enter a day number for the menu you would like to print (1-{}): ".format(len(menu))))   #Ask user to enter the day they would like to print the menu for


print_meal_plan(menu[day_num - 1])      #Call the print_meal_plan function with the menu for the selected day as a argument
