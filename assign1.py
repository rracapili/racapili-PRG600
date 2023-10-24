'''
Name: Ronald Capili
Student ID: 152344222
Description: Assignment1 Shopping Calculator
'''

def checkdiscount(item,numberofitems,price):
    """
    This function takes in item name, number of item and item price as input parameters
    and checks if the item is in the discounted items list, and returns discounted price.
    """
    discounteditems=["candy","eggs","flour","hummus","ice cream","chicken soup","diapers"]          #Initialize all discounted items
    discountrate=0.05           #Initialize minimum discount rate
    maxdiscount=0.2             #Initialize maximum discount rate
    if item in discounteditems:             #Checek if item is in discounted items list
        if discountrate * (numberofitems-1) > maxdiscount:      #If total discount exceeds 20% discount, cap discount at 20%
            discountrate = maxdiscount
        else:
            discountrate = discountrate* (numberofitems-1)      #Calculate discount rate per item if it doesn't exceed max discount
        discountedprice=price - (price*discountrate)            #Calculate discounted price and return discounted price
    else:
        discountedprice=price
    return discountedprice

def printreceipt(allitems,numberofitems,allprices,totaldiscount):
    """
    This function takes in all item list, number of items list, all prices list, and the total discounts or total savings
    and prints them in proper alignment to show all items, number of items, price per item, total price for the items,
    total sales and total savings.
    """
    totalprices=0       #Initialize totalprices to 0
    x=0                 #Initialize x for For Loop
    print("\nRECEIPT")            #Print Receipt Header
    for x in range(x,len(allitems)):            #Go through all the items in the list to print the following:
        print(x+1,end=". ")                     #Number of Item
        print("{0:<15}".format(allitems[x]),end="")         #Item name
        print("{0:<3}".format(numberofitems[x]),end="")     #Number of items
        print(" x $ ",end="")
        print("{0:<6.2f}".format(allprices[x]),end="")      #Price of item / after discount price
        print(" = $ ",end="")
        print("{0:<6.2f}".format((allprices[x]*numberofitems[x])))      #Total per item
        totalprices=totalprices+(allprices[x]*numberofitems[x])
    print("Total: ",end="")
    print("{0:>30}".format("$"),end="")
    print("{0:>5.2f}".format(totalprices))              #Total of all items
    print("You saved: ",end="")
    print("{0:>26}".format("$"),end="")
    print("{0:>5.2f}".format(totaldiscount))            #Total discount

def initialinputs():
    """
    This is the main function where user is asked to enter items, prices and number of items.
    """
    allitems=["candy","eggs","flour","hummus","ice cream","chicken soup","diapers","pork","soup","beef","milk","coffee"]        #Initialize all shop items
    entereditems=[]         #item name list
    enteredprices=[]        #item price list
    enterednumbers=[]       #item numbers list
    printallitems=', '.join(allitems)       #Used for printing all available items in the shop
    foodnumber=0            #Initialize food number to 0
    totalsavings = 0        #Initialize total savings to 0
    discountprice=0
    print("Shopping Calculator")        #Print program header
    while True:         #Loop to keep asking user for input until user decides to exit
        fooditem = input("Please enter an item of food, or press Enter to exit: ")
        if fooditem == "":          #When user presses enter without any item, print receipt if enterednumbers list is not empty
            if len(enterednumbers) > 0:
                printreceipt(entereditems,enterednumbers,enteredprices,totalsavings)
            else:
                print("Shopping Calculator Closed.")                #Close app if there are no items entered. 
            break       #Breaks loop for valid user FOODITEM or EXIT user input.
        else:           #If user enters a string
            fooditem.lower()            #put string to lower case before comparison
            if fooditem in allitems:    #Check if item is in the all shop items, if not, display error and all available items list. 
                entereditems.append(fooditem)       #If within shop items, save to entereditems list
                while True:         #Loop to catch invalid input for price. 
                    try:            #Try and except loop to make sure price input is a float
                        foodprice=float(input("Item is: %s. Please enter the price for this item: " %fooditem))
                        if foodprice > 0.00:        #Error handling for price with 0.00 price. 
                            while True:             #Loop to catch invalid input for number of food or items. 
                                foodnumber=input("Item is: %s. How many will you purchase: " %fooditem)
                                if foodnumber.isnumeric():          #Error handling for number of items, needs to be number and greater than 0. 
                                    foodnumber=int(foodnumber)      #If valid digit, convert to int
                                    if foodnumber > 0:              #If greater than 0, save as item number
                                        enterednumbers.append(foodnumber)
                                        if foodnumber > 1:          #If number of item is greater than 1, check if eligible for discount
                                            discountprice=checkdiscount(fooditem,foodnumber,foodprice)      #Call discount checker for discounted price
                                            totalsavings = totalsavings + (foodnumber*(foodprice - discountprice))  #Calculate totaldiscount before round function
                                            discountprice = round(discountprice,2)      #Round off discounted price
                                            enteredprices.append(discountprice)         #Save rounded off discounted price
                                        else:
                                            enteredprices.append(foodprice)             #If itemnumber is not greater than one, no discount
                                        break       #Breaks loop for valid ITEMNUMBER user input.
                                    else:
                                        print("Error: all items are sold in whole units and cannot be zero.")
                                else:
                                    print("Error: all items are in valid digits. Example: Enter '1' for 1 bag of flour.")
                            break       #Breaks loop for valid ITEMPRICE user input
                        else:
                            print("Error: all prices are greater than 0.00.")
                    except ValueError:
                        print("Error: price must be a number. Example: 1, or 1.99")
            else:
                print("\nError: item not found.\nPlease check the following items on sale: %s" %printallitems)     #Error message for invalid food input


if __name__ == "__main__":
    """
    Main code block to run the code
    """
    initialinputs()