#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re

# Create phone regex.
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    ([a-zA-Z0-9.%_+-]+) # email 
    (@)                 # @ symbol
    ([a-zA-Z0-9-.]+)    # domain name
    (\.co\.uk|\.[a-zA-Z]+)   # .something, eg. .com/co.uk/etc....
)''', re.VERBOSE)

# Find matches in clipboard text.
text = pyperclip.paste()
phoneOutput = phoneRegex.findall(text)
emailOutput = emailRegex.findall(text)

phoneNumbers = []
for number in phoneOutput:
    phoneNum = ('-'.join([number[1], number[3], number[5]]))
    if number[8] != '':
        phoneNum += 'x' + number[8]
    phoneNumbers.append(phoneNum)
emailAddresses = [email[0] for email in emailOutput]

# TODO: Copy results to the clipboard.
results = '\n'.join(phoneNumbers + emailAddresses)
if len(results) > 0:
    pyperclip.copy(results)
    print('Copied to clipboard: ')
    print(results)
else: 
    print('no phone numbers or emails detected')

