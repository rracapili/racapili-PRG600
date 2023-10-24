'''
Name: Ronald Capili
Student ID: 152344222
Description: Every Second Animal
'''

animals = ['snake','hamster','scorpion','beaver','mosquito','camel','vulture','horse','python','capybara']      #Initialize contents of list

x=1         #for loop counter and index for every second animal. 

for x in range(x, len(animals), 2):         #Start with second animal and print every second animal
   print(animals[x])