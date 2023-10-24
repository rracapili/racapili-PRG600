'''
Name: Ronald Capili
Student ID: 152344222
Description: Binary Converter
'''

binaryconvert = [0,0,0,0,0,0,0,0]            #Initial binary value
binarybit = 7                               #Initialize binary bit to last bit

user_decimal = int (input ("Enter a decimal number to convert to binary: "))        #User inputs decimal value
while binarybit >= 0:           #Keep doing conversion until last binary bit
    if user_decimal == 1:       #When decimal value is down to 1, set current binary bit to 1 and exit loop
        binaryconvert[binarybit] = user_decimal
        break
    else:
        binaryconvert[binarybit] = user_decimal % 2         #Get remainder of decimal value as binary bit for current binary bit
        binarybit -= 1                                      #Decrement binary bit to move on to next bit
        user_decimal = user_decimal // 2                    #Divide decimal value by 2 to slowly get to most significant bit
print (*binaryconvert)                                      #Print Binary Value