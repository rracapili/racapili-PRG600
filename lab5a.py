'''
Name: Ronald Capili
Student ID: 152344222
Description: SUMMING CALCULATOR / AVERAGE CALCULATOR
'''

'''
my_list = [] # square brackets indicate that this is a list
my_list2 = [3, 3.14, [0, 1], 'potato'] # this list contains a combination of datatypes

user_numbers = []
print("SUMMING CALCULATOR")
while True:
    user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ")
    if user_input == "":
        break
    else:
        user_numbers.append(int(user_input))
print(user_numbers)
print("Thank you for using summing calculator. The final sum was " + str(sum(user_numbers)) + ".")
'''

def my_sum(allnum):           #Calculates for the sum of all numbers on the list
    total = 0
    x = 0
    for x in range(x, len(allnum)):
        total += allnum[x]
    return total
        

if __name__ == "__main__":
    user_numbers = []
    print("SUMMING CALCULATOR")
    while True:
        user_input = input("Enter a number to add to your sum. Pressing Enter will exit. ")
        if user_input == "":
            break
        else:
            user_numbers.append(int(user_input))
    num_sum=my_sum(user_numbers)
    #num_sum = sum(user_numbers)
    #num_length = len(user_numbers)
    #average = num_sum / num_length
    #print(f"Total sum is: {num_sum}. Total count is: {num_length}. Average for this list is: {average}.")
    print(f"Total sum is: {num_sum}.")
    print("Thank you for using summing calculator.")