#!/usr/bin/python3

import pyperclip
import re

# Regex for US phone numbers
regexPhone = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code - US!
     (\s|-|\.)?                     # separator
     (\d{3})                        # first 3 digits
     (\s|-|\.)                      # separator
     (\d{4})                        # last 4 digits
     (\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
     )''', re.VERBOSE)))


# Regex for email addresses
regexEmail = .compile(r'''(
    [a-zA-Z0-9._%+-]+    # name of the user
    @                    # @ symbol
    [a-zA-Z0-9.-]+       # name of the domain
    (\.[a-zA-Z]{2-4})    # com, org, be, ...
    )''', re.VERBOSE)    

# Find matches in clipboard text
text = str(pyperclip.paste())

# Store the matches in a list
matches = []  

# Standardize the format (US) before appending each match
for groups in regexPhone.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
    
for groups in regexEmail.findall(text):
    matches.append(groups[0])
    
# TODO: find pyperclip equivalent for WSL

