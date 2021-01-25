import pyinputplus as pyip

response = pyip.inputNum(allowRegexes=[r'(C)+'])
print(response)

#result = pyip.inputMenu(['edam', 'cheddar', 'stilton'], numbered=True, limit = 3, timeout = 5) # max of three attempts, 5 second timeout
# print(result)