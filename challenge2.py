'''
Name: Ronald Capili
Student ID: 152344222
Description: Challenge
'''

print("Let's round off decimals!")
decimal_input = float(input("Enter a decimal number: "))            #User Input
rounded_int = int(decimal_input)                                    #Conversion for later computation
remaining_decimal = decimal_input - rounded_int                     #Get Decimal Value after Whole Number

if remaining_decimal <= 0.5:                                         #If Decimal value is less than .6
    print("Your whole number conversion is: " + str(rounded_int))   #Keep Whole Number Value
else:                                      #Else, add 1 to Whole Number Value
    rounded_int = rounded_int + 1
    print("Your whole number conversion is: " + str(rounded_int))