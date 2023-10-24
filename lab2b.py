'''
Name: Ronald Capili
Student ID: 152344222
Description: lab1b.py / Tax Calculator
'''

#Initialization Start - Set Values for Tax Rates, Deduction Rates
INCOME_BRACKET1 = 32000.00
INCOME_BRACKET2 = 64000.00
TAX_RATE1 = .10
TAX_RATE2 = .15
TAX_RATE3 = .25
STANDARD_DEDUCTION = 10000.00
ADDITIONAL_DEDUCTION = 2000.00
#Initialization End

#Input Start
#print("Let's calculate your tax!")
gross_income = float(input("Enter your gross income: "))            #Convert str input to float
dependents = int(input("Enter the number of dependents: "))         #Convert str input to int
#Input End

#Calculation Process Start
total_deduction = STANDARD_DEDUCTION + (ADDITIONAL_DEDUCTION * dependents)      #Calculate Total Deduction
taxable_income = gross_income - total_deduction                                 #Calculate Taxable Income

if gross_income < INCOME_BRACKET1:                #If Taxable Income is less than 32000.00
    income_tax = taxable_income * TAX_RATE1         #Tax Rate is 00.10
    #print("Your Tax Rate is: %.2f" % TAX_RATE1)
elif gross_income < INCOME_BRACKET2:              #If Taxable Income is equal to 32000.00 but less than 64000.00
    income_tax = taxable_income * TAX_RATE2         #Tax Rate is 00.15
    #print("Your Tax Rate is: %.2f" % TAX_RATE2)
else:
    income_tax = taxable_income * TAX_RATE3         #If Taxable Income is greater than 64000.00
    #print("Tax Rate is: %.2f" % TAX_RATE3)          #Tax Rate is 00.25

if income_tax <= 0:                                 #If Income Tax is less than 00.00
    income_tax = 0.00                              #Income Tax is set to 00.00

#Calculation Process End

#Output Section Start
#print("Your Total Deduction is: %.2f" % total_deduction)
#print("Your Taxable Income is: %.2f" % taxable_income)
#print("Your Total Income Tax is: %.2f" % income_tax)
print("The income tax is $%0.0f" % income_tax)
#Output Section End