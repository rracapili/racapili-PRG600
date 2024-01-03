'''
Name: Ronald Capili
Student ID: 152344222
Description: Reverse Reading
'''

import sys

print(sys.argv)                 #Prints all argumensts - all contents of the list sys.argv

if len(sys.argv) == 1:          #If no filename set, use readmet.txt
    f = open('readme.txt', 'r') #Open file
    lines=f.readlines()              #Read all lines
else:                           #Use file set
    f = open(sys.argv[1], 'r')  #Open file
    lines=f.readlines()              #Read all lines
f.close()                       #Close file
for lineprint in reversed(lines):       #Print lines in reverse
    print(lineprint.strip('\n'))