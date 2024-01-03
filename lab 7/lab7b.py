'''
Name: Ronald Capili
Student ID: 152344222
Description: Print A Menu
'''


def print_meal_plan(meal_plans):    #Function that takes a dictionary as its parameter.
    width = 50 #Initialize a width to format the printed menu Width to format the printed menu
    
    
    print(f"{'MENU FOR TODAY' : ^{width}}") #Print the header for the menu for today centered with a width of 50
    print("=" * width)                      #Print a border line with the same number of characters as the width
    
    
    print(f"{'Breakfast' : <25}{meal_plans['breakfast'] : >25}")        #Print the breakfast, lunch, and dinner menu with better formatting.
    print(f"{'Lunch' : <25}{meal_plans['lunch'] : >25}")
    print(f"{'Dinner' : <25}{meal_plans['dinner'] : >25}")


meal_plan = {'breakfast': 'oatmeal', 'lunch': 'sandwiches', 'dinner': 'broccoli'}   #Initialize Meal Plan Dictionary


if __name__ == "__main__":
    """
    Main code block to run the code
    """
    print_meal_plan(meal_plan)  #Call print_meal_plan function with the meal_plan dictionary
