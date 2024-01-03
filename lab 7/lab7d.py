'''
Name: Ronald Capili
Student ID: 152344222
Description: Substitute Data In A CSV File
'''

#Import csv and sys modules
import csv
import sys

def readcsv(filename):      #Function to read the contents of the CSV file
    '''
    This function will read the CSV file and return it as a list
    '''
    list_of_dicts = []          #Initialize list_of_dicts
    f = open(filename, 'r')     #Open file
    reader = csv.DictReader(f)  #Read CSV to a dictionary

    for row in reader:      #Iterate through each row in the read CSV and append it to the list_of_dicts
        list_of_dicts.append(row)
    f.close()

    return list_of_dicts    #Return list_of_dicts with the read CSV file as dictionaries inside the list_of_dicts.


def writecsv(filename, listofdicts):        #Function to write a list of dictionaries to a CSV file
    '''
    This function will write in the CSV file using a list of dictionaries. 
    '''
    f = open(filename, 'w')         #Open the file
    fieldnames = listofdicts[0].keys()      #Get the first row as fieldnames for each column in the CSV file.
    w = csv.DictWriter(f, fieldnames=fieldnames)    #Set the field names for the CSV file. 
    
    w.writeheader()     #Write the header for the CSV file. 
    
    for row in listofdicts:     #Iterate through each dictionary in the list, and modify the values
        try:
            if row["First Name"] == "Christopher":
                row["First Name"] = "Chris"
            if row["Last Name"] == "Patal":
                row["Last Name"] = "Patel"
            elif row["Last Name"] == "Smith":
                row["Last Name"] = "Nichols"
            elif row["Last Name"] == "Geary":
                row["Address"] = "455 Bloor"
            if row["Address"] == "81 Vanier":
                row["Address"] = "72 Princeton"
            if row["City"] == "North York":
                row["City"] = "Toronto"
            if row["Country"] == "Canada":
                row["Country"] = "CA"
        except KeyError as e:               #Handle KeyError Exceptions
            print("Handling key error" + str(e))    #Print error message
        w.writerow(row)     #Write the modified dictionary as rows in the CSV file. 
    f.close()       #Close file. 

if len(sys.argv) == 1:      #Error handling for proper usage and number of arguments
    print("Usage: lab7d.py filename")
else:           #Save the filename from the second argument
    filename = sys.argv[1]
    outfile = "out_" + filename     #Create an output file with a different filename by adding "out" as a prefix

    try:
        writecsv(outfile, readcsv(filename))        #Call writecsv function with outfile as first argument, and the return list from calling the readcsv function
    except FileNotFoundError:                       #Print error messsage if file is not found.
        print("ERROR: %s not found." % filename)
