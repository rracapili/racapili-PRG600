'''
Name: Ronald Capili
Student ID: 152344222
Description: Function Examples
'''

from random import randint

def rtrn_area(length, width): # Computes for Area using Length and Width
    "Uses arguments as Length and Width to compute and return Area"
    return length * width

def print_all_caps(name, age): # Converts and prints name input in all capital letters together with age
    "Converts first arguent (name) to all capital letters and prints it along with the second argument (age)."
    cap_name = name.upper()
    print('THIS PERSON\'S NAME IS ' + cap_name + ' AND THEY ARE ' + str(age) + ' YEARS OLD!!!')

def get_rando(): # Generate a random number
    "Return a random number between 1 and 101"
    return randint(1,101)

def is_odd(num): # Returns boolean value if number is odd
    "Returns True if number is odd and False if number is not odd."
    if num % 2 == 1:
        return True
    else:
        return False

if __name__ == "__main__":
    rect = rtrn_area(5, 3)
    # call the function again with new values
    rect = rtrn_area(6, 2)
    print(str(rect))

    print_all_caps('eric', 41)
    print_all_caps('melissa', 40)
    # call the function again with new values
    print_all_caps('ronald', 35)

    lucky_num = get_rando()
    # call the function again with new values

    test_lucky_num = get_rando()
    print(str(test_lucky_num))

    print(is_odd(13))
    print(is_odd(get_rando()))
    # call the function again with new values
    print(is_odd(27))