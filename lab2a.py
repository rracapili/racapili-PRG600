'''
Name: Ronald Capili
Student ID: 152344222
Description: lab1b.py / Math Calculations / String Conversion and Print
'''
#User Inputs Start
user_num1 = input ("Enter the first number: ")              #Enter first number
user_num2 = input ("Enter the second number: ")             #Enter second number
#User Inputs End

#Conversion Start
user_int1 = int(user_num1)
user_int2 = int(user_num2)
#Conversion End

result = user_int1 + user_int2

#Output Print Start
print ("\nThe result of " + str(user_int1) + " plus " + str(user_int2) + " is: " + str(result))
#Output Print End