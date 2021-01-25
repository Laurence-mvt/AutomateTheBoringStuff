import re

def checkPassStrength(password):
    # check 8 characters in length
    passLength = len(password)
    if passLength < 8:
        print('8 characters minimum')
        return False

    # check at least one upper and lower case
    lowerRegex = re.compile(r'(\S| )*[a-z](\S| )*')
    mo1 = lowerRegex.search(password)
    if mo1 == None:
        print("one lower case character required")
        return False
    
    # check at least one digit
    upperRegex = re.compile(r'(\S| )*[A-Z](\S| )*')
    mo2 = upperRegex.search(password)
    if mo2 == None:
        print("one UPPER case character required")
        return False
    
    # if passed, then password accepted
    print('Password accepted')
