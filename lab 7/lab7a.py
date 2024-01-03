'''
Name: Ronald Capili
Student ID: 152344222
Description: Understanding the Limitations of Lists
'''

def shipping_label(a_dict):         #Function to take list as parameter.
    a_str = f"{str(a_dict['first_name']).capitalize()} {str(a_dict['last_name']).capitalize()}\n"  #Combine first and last name with a newline at the end.
    a_str += f"{a_dict['addr1']}\n"  #Add addr1 with a newline at the end.
    a_str += f"{a_dict['city']}, {a_dict['prov']}\n"  #Add city with a comma, space and the province with a newline at the end.
    a_str += f"{a_dict['pcode']}"  #Add the pcode
    
    # Return the final shipping label string.
    return a_str

# student1 dictionary
student1 = {'first_name': 'eric', 'last_name':'smith', 'addr1': '217 Au Large Blvd', 'city': 'Toronto', 'prov': 'Ontario', 'pcode': 'M4A 1P3'}
# Call the shipping_label function with the student1 data and print the result.
print(shipping_label(student1))
