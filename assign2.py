'''
Name: Ronald Capili
Student ID: 152344222 / radcapili
Description: Store Stock Calculator
'''

import sys
import csv

def exportstocks(exportfile,newstocks):
    """
    Function to export updated stocks to export file. This function requires the export filename, and the newstocks list of dictionaries.
    """
    with open(exportfile, 'w', newline='') as f:                #Use with Open so we can set newline to '' so no extra newline will be printed after every row.
        fieldnames = newstocks[0].keys()                        #Get field names using .keys()
        w = csv.DictWriter(f,fieldnames=fieldnames)             #Set the fieldnames using csv.DictWriter(<opened file variable,fieldnames=<fieldname variable>)
        w.writeheader()                                         #Write the field names using .writeheader()
        for row in newstocks:                                   #Begin writing the values for the keys in the list of dictionaries. 
            w.writerow(row)

def getlongname(stocks):
    """
    Function to get longest item name in read stocks and returns the length of the longest name. Function takes read stocks as an argument. 
    """
    longname = 0 
    for stock in stocks:            #Go through the dictionary and find the longest item name
        if len(stock['Item']) > longname:
            longname = len(stock['Item'])           #Save the length of the longest item name
    return longname                 #Return the longest item name length

def printstocks(stocks,longname):
    """
    Function to print current stocks. This function requires the current stocks list of dictionaries, and longest item name length, as arguments.
    """
    print()                         #Print extraline  
    print(f"{'#':<4}{'Item':<{longname+5}}{'Current Stock':<17}{'Price per Item':<14}")         #Print header with formatting based on the longest item name
    print('='*(longname+40))                                                                    #Print separator  with formatting based on the longest item name
    for item_number, stock in enumerate(stocks, start=1):                                       #Iterate through stocks and print each item with proper formatting
        print(f"{str(item_number)+'.':<4}{stock['Item']:<{longname+11}}{stock['Current Stock']:<15}$ {stock['Price per Item']:<4.2f}")

def printsales(stocks,total_sales,total_price,longname):
    """
    Function to print total sales. This function requires the current stocks list of dictionaries, list of total sales, list of total sales price,
    and longest item name length as arguments. 
    """
    print()                         #Print extraline
    print("Total Sales")            #Print Total Sales Label
    print(f"{'#':<4}{'Item':<{longname+5}}{'Sales':<9}{'Price per Item':<19}{'Total':<4}")          #Print header with formatting based on the longest item name
    print('='*(longname+42))                                                                        #Print separator  with formatting based on the longest item name
    for item_number, stock in enumerate(stocks, start=1):       #Iterate through stocks and print each corresponding sales per item with proper formatting
        print(f"{str(item_number)+'.':<4}{stock['Item']:<{longname+7}}{total_sales[item_number-1]:<11}$ {stock['Price per Item']:<11.2f}$ {total_price[item_number-1]:<7.2f}")
    print(f"{'TOTAL':<{longname+35}}$ {sum(total_price):<7.2f}")                                    #Print total sales

def printlostsales(stocks,lost_sales,lost_price,longname):
    """
    Function to print lost sales. This function requires the current stocks list of dictionaries, list of lost sales, list of lost sales price,
    and longest item name length as arguments. 
    """
    print()                         #Print extraline
    print("Lost Sales")             #Print Lost Sales Label
    print(f"{'#':<4}{'Item':<{longname+5}}{'Sales':<9}{'Price per Item':<19}{'Total':<4}")          #Print header with formatting based on the longest item name
    print('='*(longname+42))                                                                        #Print separator  with formatting based on the longest item name
    lostsalesnum = 1                #Initialize a number starting from 1 to count lost sales items. 
    for item_number, stock in enumerate(stocks, start=1):       #Iterate through stocks and print each corresponding lost sales per item with proper formatting
        if lost_sales[item_number-1] > 0:                       #If a particular item has no lost sale, don't print the item
            print(f"{str(lostsalesnum)+'.':<4}{stock['Item']:<{longname+7}}{lost_sales[item_number-1]:<11}$ {stock['Price per Item']:<11.2f}$ {lost_price[item_number-1]:<7.2f}")
            lostsalesnum += 1                                   #Increment lostsales count number everytime a lost sales item is printed
    print(f"{'TOTAL':<{longname+35}}$ {sum(lost_price):<7.2f}")                                     #Print total lost sales

def printstockreport(stocks,total_sales,lost_sales,longname):
    """
    Function to print restock report and return list of total demand for items. This function requires the current stocks list of dictionaries, list of total sales, list of lost sales,
    and longest item name length as arguments. 
    """
    from_warehouse = 0      #Initialize from warehouse value to 0
    items_totaldemand = []  #Initialize all items total demand
    print()                         #Print extraline
    print("Restock Report")         #Print Restock Label
    print(f"{'#':<4}{'Item':<{longname+5}}{'Demand':<9}{'20%':<6}{'Total Demand':<15}{'Current Stock':<16}{'From Warehouse':<14}") #Print headers
    print('='*(longname+69))                                                                        #Print separator  with formatting based on the longest item name
    for item_number, stock in enumerate(stocks, start=1):       #Iterate through stocks and print each corresponding restock report per item with proper formatting
        demand=total_sales[item_number-1]+lost_sales[item_number-1]                         #Calculate demand for the day
        demand20 = round((total_sales[item_number-1]+lost_sales[item_number-1])*.2)         #Calculate 20% of demand for the day
        total_demand = (total_sales[item_number-1]+lost_sales[item_number-1])+(round((total_sales[item_number-1]+lost_sales[item_number-1])*.2))    #Calculate total demand
        if stock['Current Stock'] > total_demand:               #From warehouse value calculation
            from_warehouse = 0                                  #If current stock greater than total demand, leave from warehouse value to 0
        else:                                                   #Else, calculate from warehouse by deducting current stock from total demand
            from_warehouse = total_demand - stock['Current Stock']
        items_totaldemand.append((stock['Current Stock']+from_warehouse))                  #Append total demand of an item to list of all items total demand
        print(f"{str(item_number)+'.':<4}{stock['Item']:<{longname+7}}{demand:<8}{demand20:<11}{total_demand:<14}{stock['Current Stock']:<18}{from_warehouse:<7}") #Print Report
    return items_totaldemand

def readfile(in_filename):
    """
    Function to read file contents - Read CSV file and return list of dictionaries 
    """
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
    
    listofdicts = []                    #Initialize list of dictionary for items in CSV File
    csvreader=csv.DictReader(f)                                 #read file
    for row in csvreader:                                       #Convert Current Stocks key value to integer, and Price per Item key value to float
        row['Current Stock'] = int(row['Current Stock'])
        row['Price per Item'] = float(row['Price per Item'])
        listofdicts.append(row)                                 #Update converted values
    f.close()                                           #close file
    return listofdicts


if __name__ == "__main__":
    """
    Main code block to run the code
    """
    if len(sys.argv) < 2 or len(sys.argv) > 3:                       #Check if usage is proper. If no file is entered, print usage instructions. 
        print ("Usage: assign2.py <stocks-filename> <optional file-filename to export updated stocks")
    else:
        filename = sys.argv[1]
        stocks=readfile(filename)           #Read currentstocks from CSV file in commandline argument
        longname = getlongname(stocks)      #Call getlongname to get longest item name length for print formatting
        total_sales = [0 for i in range(len(stocks))]           #Initialize a total sales count list with the same number of elements as the number of items
        total_price = [0 for i in range(len(stocks))]           #Initialize a total price list with the same number of elements as the number of items
        lost_sales = [0 for i in range(len(stocks))]            #Initialize a lost sales count list with the same number of elements as the number of items
        lost_price = [0 for i in range(len(stocks))]            #Initialize a lost price list with the same number of elements as the number of items
        printstocks(stocks,longname)                                     #Call print function to print initial stocks values

        while True:                     #Main loop to keep asking user for input until user decides to terminate program
            user_input = input(f"Select a number (1-{len(stocks)}) to indicate a sale, or 'e' to indicate end of day: ")        #Ask user input
            if user_input.lower() == 'e':               #Exit if user enter 'e'
                break
            elif user_input.isnumeric():                #If user enters a numeric value, check for valid input
                number_input = int(user_input)          #Convert input to int data type
                if number_input < 1 or number_input > len(stocks):      #If value is outside the items number range, print error message
                    print("Error: Invalid input.")
                else:
                    for item_number, stock in enumerate(stocks, start=1):   #If value is valid, proceed with calculation process
                        if number_input == item_number:                     #Iterate through the list of dictionaries and look of the item number
                            if stock['Current Stock'] == 0:                 #If current stock for item number is already 0, count input to lost sales
                                lost_sales[number_input-1] += 1             #Increment lost sales
                                lost_price[number_input-1] = lost_sales[number_input-1] * stock['Price per Item']       #Calculate total lost sales for the item number
                            else:
                                stock['Current Stock'] -= 1                 #If current stock is greater than 0, decrement it
                                total_sales[number_input-1] += 1
                                total_price[number_input-1] = total_sales[number_input-1] * stock['Price per Item']     #Calculate total sales for the item number
                    printstocks(stocks,longname)                                     #Print current item stocks
            else:
                print("Error: Invalid input.")                              #Print error message for invalid input
        printsales(stocks,total_sales,total_price,longname)                 #Call total sales print function
        printlostsales(stocks,lost_sales,lost_price,longname)               #Call lost sales print function
        items_totaldemand=printstockreport(stocks,total_sales,lost_sales,longname)            #Call restock report print function

    if len(sys.argv) == 3:          #If there is an extra argument for an output file for update stocks file
        exportfile = sys.argv[2]    #Save file name for export file
        newstocks=stocks            #Initialize export file contents with current stocks
        for stock in newstocks:     #Convert all Current Stock to integer
            stock['Current Stock'] = int(stock['Current Stock'])
        for item_number, stock in enumerate(newstocks, start=0):        #Update current stock with the updated stocks - sum of current stocks and from warehouse stocks
            stock['Current Stock'] = items_totaldemand[item_number]
        exportstocks(exportfile,newstocks)                              #Call file export function to export to export filename
        