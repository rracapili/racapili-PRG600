'''
Name: Ronald Capili
Student ID: 152344222
Description: Circle Area Calculator
'''
import math

def circle_area(radius):        #Computes for a circle's area using radius as an input
    "Uses argument as input for radius to compute for a circle's radius"
    return math.pi * (radius**2)        #Compute for Circle Area pi*r**2

if __name__ == "__main__":              #Perform only on main block
    user_input = 0                      #Initialize User Input to 0
    print("Circle Area Calculator")
    while user_input != '':             #While user input is not Enter
        user_input = input("Enter a radius between 0 and 1999. Press Enter to exit: ")      #Ask for radius input
        if user_input.isnumeric():                  #Check if not a number input
            if -1 < int(user_input) < 2000:         #Check if input is within range
                user_input = int(user_input)        #Convert input to integer
                area = circle_area(user_input)      #Call circle_area calculator function
                print("Radius: %s. Area is: %s." %(user_input, area))           #Print results
            else:
                print("Error: %s is out of range." %(user_input))               #Error if input is out of range
        elif user_input == '':                                                  #Exit program when user inputs Enter
            print("Exiting...")
            break
        else:
            print("Error: %s is not a number." %(user_input))                   #Error if input is not a number