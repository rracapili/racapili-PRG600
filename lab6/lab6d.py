'''
Name: Ronald Capili
Student ID: 152344222
Description: Text Parser
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
    #samplefile = "sampleout.txt"
    print(sys.argv)                 #Prints all argumensts - all contents of the list sys.argv
    newlines = []                   #Initialize newlines list for the new contents of the file - no numbers
    totals = []                     #Initialize totals list
    if len(sys.argv) < 2:          #If there are missing arguments
        print("Usage: lab6d.py filename")       #Print sensible error message.
    else:                           #Process arguments
        lines=read_file(sys.argv[1])        #Call read_file function
        #for lineprint in lines:       #Print lines
        #    print(lineprint.strip('\n'))
        for eachline in lines:          #Process each line for separation
            nline = []                  #Initialize a blank line for the new line to be printed in the file
            total = 0.00                #Initialize the total float in a line to 0
            words=eachline.split()      #Remove spaces in each line
            for w in words:             #Go through each element in the line
                try:                    #Use try to figure out if an element is a valid numeric value or not
                    total += float(w)   #If a it's a valid number, convert to float and at to total float in a line
                except:                 #If not a valid number value, then it's treated as a string
                    nline.append(w)    #Add to new line to be printed in the file
            nline=' '.join(nline)
            newlines.append(nline)      #Append the line with the numbers removed to the newlines list for printing in the file
            totals.append(total)        #Append the total floats in the line to the totals list
        samplefile = sys.argv[1]
        with open(samplefile, 'w') as newfile:          #Start writing the lines without numbers in the file
            for printlines in newlines:                 #Print each line
                newfile.write(printlines + "\n")        #Put new line after each line
        for printtotals in totals:                      #Print all totals of float per line
            print(printtotals)                          #Printing each total


        #print(newlines)
        #print(totals)
