'''
Name: Ronald Capili
Student ID: 152344222
Description: Average Calculator
'''

import sys          #Enables the use of sys functions for command line arguments such as sys.argv, sys.exit

print(sys.argv[0] + "\n")          #Print file ran

numberinput = 0             #Initializations for Average computation
numbersum = 0
average = 0.0

if len(sys.argv) == 1:          #If no arguments passed
    print("Usage: Enter one or more command line arguments.")
    sys.exit(1)
else:                           #If there are arguments passed
    x=1                         #Check arguments for numbers and compute for average
    for x in range (x, len(sys.argv)):
        if sys.argv[x].isnumeric():
            print("Number found: %s." %sys.argv[x])
            numberinput += 1            #If numeric, increment numberinput to count total number of numbers
            numbersum += int(sys.argv[x])
        else:
            print("Error: %s is not a number." %sys.argv[x])
    #print("Thank you! Program succeeded.")
    average = numbersum / numberinput
    print("Average for %s numbers: %s." %(numberinput, average))
    sys.exit(0)