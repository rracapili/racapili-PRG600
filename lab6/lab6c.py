'''
Name: Ronald Capili
Student ID: 152344222
Description: A Simple Grep
'''

import sys

def read_file(filename):
    """
    Read file with exception handling. Takes filename as parameter and returns the read file. 
    """
    try:                            #try block to check if file exists, readable, and does't show any other error after read
        f=open(filename, 'r')       #open file
    except FileNotFoundError:       #Check if file exists
        print(f"ERROR: {filename} not found.")          #Print Error message
        sys.exit(1)                                     #Halt operation with exit code 1
    except PermissionError:                             #Check if file can be read
        print(f"You do not have permission to open {filename}.")            #Print Error message
        sys.exit(1)                                     #Halt operation with exit code 1
    except:                                             #Check for any other error available
        print("Something has gone wrong, but we know it isn't a permission error or file not found error.")         #Print Error message
        sys.exit(2)                                     #Halt operation with exit code 2
    lines=f.readlines()                                 #read lines
    f.close()                                           #close file
    return lines                                        #Return read lines


if __name__ == "__main__":
    """
    Main code block to run the code
    """
    print(sys.argv)                 #Prints all argumensts - all contents of the list sys.argv
    if len(sys.argv) < 3:          #If there are missing arguments
        print("Usage: lab6c.py keyword filename")       #Print sensible error message.
    else:                           #Process arguments
        keyword = sys.argv[1]       #Save keyword to look for
        lines=read_file(sys.argv[2])        #Call read_file function
        x=0                                 #Initialize x to be used in for loop
        for x in range(x,len(lines)):       #Loop through all the elements in the lines list
            if keyword in lines[x]:         #Check if keyword is found within an element / line
                print(str(x+1) + ": " + lines[x].strip('\n'))       #If found, print line number and the line
                #print(f"{x+1}: {lines[x].strip('\n')}")
        
#        for lineprint in lines:       #Print lines
#            print(lineprint.strip('\n'))