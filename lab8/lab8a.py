'''
Name: Ronald Capili, Daniel Obaze, Julius Ugwu
Student ID: radcapili, cdobaze, jiugwu
Description: RE Module: Using Search
'''

'''
Research: 
This module provides regular expression matching operations similar to those found in Perl.

We are using the sample code provided in lab6 to test our regular expressions. 

'''

'''
Regex.txt update:
Regex : 
\d{4}-?[0-1]?[0-9]-?[0-3]?[0-9]\s?[0-2]?[0-9]
:?[0-5]?[0-9]
:?[0-5]
[0-9]\s?[a]\w*\s(\d{4}
|\d{5})$\s\w\w?[e]\s^[a-z]
[a-z0-9_]
{2,15}$
\b[a-z][a-z0-9_]{2,15}\b

Test String: 
1999-12-31
23:56:56
apple
1001
eye
a_565
telephone

Failed String:
1999-12-31
23:66:56
qpple
100133
eye
a_565
1234567891123456789
'''

import re

tel_num = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = tel_num.findall('My telephone number is 555-877-5678. Or you can reach me on my cell: 555-212-0771. Call me!')

for match in mo:
    print('Found phone number: ' + match)