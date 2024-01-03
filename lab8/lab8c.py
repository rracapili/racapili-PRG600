'''
Name: Ronald Capili
Student ID: 152344222 / radcapili
Description: System Status
'''

import os
import re

input_string = "System Boot Time: 11/16/2023, 1:12:17 AM"           #Sample String for testing
uptime_regex = re.compile(r'(System Boot Time:.*)\n')                       #Regex to capture uptime

username = os.popen('whoami')
output = username.readline()
output = output.rstrip()
print ('Welcome %s.' %(output))
pingtest = os.system('ping www.google.com')
if pingtest == 0:
    print('The Internet is UP.')
else:
    print('The Internet is DOWN.')
cap_sysinfo = os.popen('systeminfo')                                #Get systeminfo
output = cap_sysinfo.read()
uptime = uptime_regex.findall(output)                               #Find Up Time
print ('uptime is: ')
print (uptime[0])