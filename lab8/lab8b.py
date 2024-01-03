'''
Name: Ronald Capili
Student ID: 152344222 / radcapili
Description: Match Phone Numbers In A File
'''

import sys
import re

def readfile(in_filename):
    try:                            #try block to check if file exists, readable, and does't show any other error after read
        f=open(in_filename, 'r')       #open file
    except FileNotFoundError:       #Check if file exists
        print(f"ERROR: {in_filename} not found.")          #Print Error message
        sys.exit(1)                                     #Halt operation with exit code 1
    except PermissionError:                             #Check if file can be read
        print(f"You do not have permission to open {in_filename}.")            #Print Error message
        sys.exit(1)                                     #Halt operation with exit code 1
    except:                                             #Check for any other error available
        print("Something has gone wrong, but we know it isn't a permission error or file not found error.")         #Print Error message
        sys.exit(2)                                     #Halt operation with exit code 2
    fulltext=f.read()                                 #read file
    f.close()                                           #close file
    return fulltext


if __name__ == "__main__":
    if len(sys.argv) < 2:                   #If no filename set, print an error message
        print("Usage: lab8b.py filename")
    else:
        tel_num = re.compile(r'\d{3}-\d{3}-\d{4}')             #Regex to get phone numbers
        fullfile = readfile(sys.argv[1])                        #Read the file
        phonenum = tel_num.findall(fullfile)                    #Find all strings that match the regex tel_num
        print ('Found %s phone numbers in the file.' %(len(phonenum)))      #Print the number of matches found
        while True:                                                         #Ask user if they want to print the results found
            printinput = input("Do you want to see the results? Y/N: ")
            if printinput.isnumeric():
                pass
            elif printinput.lower() == 'y' or printinput.lower() == "":     
                for match in phonenum:
                    print('Found phone number: ' + match)
                break
            elif printinput.lower() == 'n':
                break
            else:
                pass