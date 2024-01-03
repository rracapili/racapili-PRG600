'''
Name: Ronald Capili
Student ID: 152344222
Description: File Writing
'''

data_to_write = ['First Line!', 'Second Line!!', 'Third Line!!!', '...and so on!']          #List of lines to print

f = open('testing.txt', 'w')            #Open / create file
for line in data_to_write:              #Write all lines from data_to_write
    f.write(line + "\n")                #Print a line and put a newline character at the end. 
f.close()                               #Close the file