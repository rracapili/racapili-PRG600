'''
Name: Ronald Capili
Student ID: 152344222 / radcapili
Description: Using os.path Methods
'''

import os
course_dir = '..'
for root, directories, filenames in os.walk(course_dir):
    for directory in directories:
        print(os.path.join(root, directory))
        for file in filenames:
            print(os.path.join(root, file))