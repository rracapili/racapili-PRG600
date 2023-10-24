'''
Name: Ronald Capili
Student ID: 152344222
Description: Working With Command Line Arguments
'''

import sys                      #Enables the use of sys functions for command line arguments such as sys.argv, sys.exit

print(sys.argv)                 #Prints all argumensts - all contents of the list sys.argv
print(f"The name of the file you are running is: {sys.argv[0]}.")

if len(sys.argv) == 1:
    print("No arguments found.")
else:
    for arg in sys.argv[1:]: # start from the second item in the list
        print(f"Argument found: {arg}.")
print("Complete.")