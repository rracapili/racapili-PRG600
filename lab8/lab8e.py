'''
Name: Ronald Capili
Student ID: 152344222 / radcapili
Description: Backup Script
'''

import os
import sys
import re
import shutil

if __name__ == "__main__":
    pythonregex=re.compile(r'.*\.py$')
    if len(sys.argv) < 2:                   #If no filename set, print an error message
        print("Usage: lab8e.py directory")      #Print error message
    else:                                       #Else, proceed with the program
        absolute_path = os.path.abspath(sys.argv[1])                    #Save Absolute path of directory
        backups = os.path.join(absolute_path, 'backups')                #Create backups path directory
        if os.path.exists(sys.argv[1]):                                 #If directory exsist, proceed to copy files
            for root, directories, filenames in os.walk(absolute_path):     #Check for all files within the directory
                for file in filenames:                                      #Check for all filenames found
                    if pythonregex.match(file):                             #Check if file is a .py file using regex
                        sourcefile=(os.path.join(root,file))                #Save source file path
                        destinationfile=(os.path.join(backups,file))        #Save backup destination file path
                        #print(sourcefile)
                        #print(destinationfile)
                        counter=1
                        while os.path.exists(destinationfile):                 #If file already exists, rename it as .bak#
                            destinationfile=(os.path.join(backups,file+'.bak'+str(counter)))        #Set new destination file path
                            counter +=1                                                             #Increment counter for number of copies
                        #print(destinationfile)
                        if not os.path.exists(backups):                         #If backups diretory doesn't exist, create directory
                            os.makedirs(backups)
                        shutil.copy(sourcefile, destinationfile)                #Proceed to copy
                #break
        else:                                                                   #If input directory doesn't exsist, print error message.
            print('ERROR: Not a valid directory.')
            #print(f"The directory '{sys.argv[1]}' does not exist.")
