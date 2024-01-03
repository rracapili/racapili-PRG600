'''
Name: Ronald Capili
Student ID: 152344222 / radcapili
Description: Store Stock Calculator
'''

import math
import sys
import csv

def printstocks(stocks):
    """
    function: Print current stocks 
    """
    longname = 0
    print()
    for stock in stocks:
        if len(stock['Item']) > longname:
            longname = len(stock['Item'])
    print(f"{'#':<4}{'Item':<{longname+5}}{'Current Stock':<17}{'Price per Item':<14}")
    print('='*(longname+40))
    for item_number, stock in enumerate(stocks, start=1):
        print(f"{str(item_number)+'.':<4}{stock['Item']:<{longname+11}}{stock['Current Stock']:<15}$ {stock['Price per Item']:<4}")
        #print(f"Item {item_number}:", stock['Item'])
        #print("Current Stock:", stock['Current Stock'])
        #print("Price per Item:", stock['Price per Item'])
        #print()  # Add an empty line for better readability

def printsales(stocks,total_sales,total_price):
    """
    Function to print total sales
    """
    longname = 0
    print()
    print("Total Sales")
    for stock in stocks:
        if len(stock['Item']) > longname:
            longname = len(stock['Item'])
    print(f"{'#':<4}{'Item':<{longname+5}}{'Sales':<9}{'Price per Item':<19}{'Total':<4}")
    print('='*(longname+42))
    for item_number, stock in enumerate(stocks, start=1):
        print(f"{str(item_number)+'.':<4}{stock['Item']:<{longname+7}}{total_sales[item_number-1]:<11}$ {stock['Price per Item']:<11}$ {total_price[item_number-1]:<7.2f}")
    print(f"{'TOTAL':<{longname+35}}$ {sum(total_price):<7.2f}")

def printlostsales(stocks,lost_sales,lost_price):
    """
    Function to print total sales
    """
    longname = 0
    print()
    print("Lost Sales")
    for stock in stocks:
        if len(stock['Item']) > longname:
            longname = len(stock['Item'])
    print(f"{'#':<4}{'Item':<{longname+5}}{'Sales':<9}{'Price per Item':<19}{'Total':<4}")
    print('='*(longname+42))
    lostsalesnum = 1
    for item_number, stock in enumerate(stocks, start=1):
        if lost_sales[item_number-1] > 0:
            print(f"{str(lostsalesnum)+'.':<4}{stock['Item']:<{longname+7}}{lost_sales[item_number-1]:<11}$ {stock['Price per Item']:<11}$ {lost_price[item_number-1]:<7.2f}")
            lostsalesnum += 1
    print(f"{'TOTAL':<{longname+35}}$ {sum(lost_price):<7.2f}")

def printstockreport(stocks,total_sales,lost_sales):
    """
    Function to print total sales
    """
    longname = 0
    from_warehouse = 0
    print()
    print("Restock Report")
    for stock in stocks:
        if len(stock['Item']) > longname:
            longname = len(stock['Item'])
    print(f"{'#':<4}{'Item':<{longname+5}}{'Demand':<9}{'20%':<6}{'Total Demand':<15}{'Current Stock':<16}{'From Warehouse':<14}")
    print('='*(longname+69))
    for item_number, stock in enumerate(stocks, start=1):
        demand=total_sales[item_number-1]+lost_sales[item_number-1]                         #Calculate demand for the day
        demand20 = round((total_sales[item_number-1]+lost_sales[item_number-1])*.2)         #Calculate 20% of demand
        total_demand = (total_sales[item_number-1]+lost_sales[item_number-1])+(round((total_sales[item_number-1]+lost_sales[item_number-1])*.2))    #Calculate total demand
        if stock['Current Stock'] > total_demand:               #From warehouse value calculation
            from_warehouse = 0                                  #If current stock greater than total deman, leave from warehouse value to 0
        else:                                                   #Else, calculate from warehouse by deducting current stock from total demand
            from_warehouse = total_demand - stock['Current Stock']
        print(f"{str(item_number)+'.':<4}{stock['Item']:<{longname+7}}{demand:<8}{demand20:<11}{total_demand:<14}{stock['Current Stock']:<18}{from_warehouse:<7}")
    #for item_number, stock in enumerate(stocks, start=1):
    #    print(f"{str(item_number)+'.':<4}{stock['Item']:<{longname+7}}{total_sales[item_number-1]:<11}$ {stock['Price per Item']:<11}$ {total_price[item_number-1]:<7.2f}")
    #print(f"{'TOTAL':<{longname+35}}$ {sum(total_price):<7.2f}")

def readfile(in_filename):
    """
    function: Read file contents - Read CSV file and return list of dictionaries 
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
    for row in csvreader:
        row['Current Stock'] = int(row['Current Stock'])
        row['Price per Item'] = float(row['Price per Item'])
        listofdicts.append(row)
    f.close()                                           #close file
    return listofdicts


if __name__ == "__main__":
    """
    Main code block to run the code
    """
    if len(sys.argv) < 2:
        print ("Usage: assign2.py <stocks-filename>.")
    else:
        filename = sys.argv[1]


        stocks1 = [
            {'Item': 'Apple', 'Current Stock': 3, 'Price per Item': 1.00},
            {'Item': 'Banana', 'Current Stock': 4, 'Price per Item': 2.50},
            {'Item': 'Orange', 'Current Stock': 5, 'Price per Item': 1.50}
        ]
        stocks=readfile(filename)           #Read currentstocks from CSV file in commandline argument
        #sales_row = {'Item': '', 'Sales': 3, 'Price per Item': 0.00, 'Total': 0.00}
        total_sales = [0 for i in range(len(stocks))]           #Initialize a total sales count list with the same number of elements as the number of items
        total_price = [0 for i in range(len(stocks))]           #Initialize a total price list with the same number of elements as the number of items
        lost_sales = [0 for i in range(len(stocks))]            #Initialize a lost sales count list with the same number of elements as the number of items
        lost_price = [0 for i in range(len(stocks))]            #Initialize a lost price list with the same number of elements as the number of items
        from_warehouse = 0                                      #Initialize from_warehouse value for printing in restock report
        printstocks(stocks)                                     #Call print function to print initial stocks values
        #print (lost_sales)
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
                    printstocks(stocks)                                     #Print current item stocks
            else:
                print("Error: Invalid input.")                              #Print error message for invalid input
        #printstocks(stocks)
        #print ("Total Sales")                           #Total sales print section
        #print (total_sales)
        #print (total_price)
        #print (sum(total_price))
        printsales(stocks,total_sales,total_price)
        printlostsales(stocks,lost_sales,lost_price)
        printstockreport(stocks,total_sales,lost_sales)
        print()
        """
        print ("Restock Report")                        #Restock report print section
        for item_number, stock in enumerate(stocks, start=1):               #Iterate through all items in the list of item dictionaries
            print(f"Item {item_number}:", stock['Item'])                    #Print item name and number
            demand=total_sales[item_number-1]+lost_sales[item_number-1]     #Calculate demand for the day
            print(f"Demand: {demand}")                                      #Print demand
            demand20 = round((total_sales[item_number-1]+lost_sales[item_number-1])*.2)         #Calculate 20% of demand
            print(f"20%: {demand20}")                                                           #Print 20% of demand
            total_demand = (total_sales[item_number-1]+lost_sales[item_number-1])+(round((total_sales[item_number-1]+lost_sales[item_number-1])*.2))    #Calculate total demand
            print(f"Total Demand: {total_demand}")              #Print total demand
            print("Current Stock:", stock['Current Stock'])         #Print current stocks for the item
            if stock['Current Stock'] > total_demand:               #From warehouse value calculation
                from_warehouse = 0                                  #If current stock greater than total deman, leave from warehouse value to 0
            else:                                                   #Else, calculate from warehouse by deducting current stock from total demand
                from_warehouse = total_demand - stock['Current Stock']
            print(f"From Warehouse: {from_warehouse}")              #Print from warehouse value
            print()
        """