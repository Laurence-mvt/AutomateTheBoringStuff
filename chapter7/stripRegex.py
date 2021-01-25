# a regex version of strip() method

"""   Write a function that takes a string and does the same thing as the strip() string method. 
If no other arguments are passed other than the string to strip, then whitespace characters will be
removed from the beginning and end of the string. 
Otherwise, the characters specified in the second argument to the function will be removed from the string.       """

import re

def regexStrip(toStrip, stripWhat = None):
    # if second argument = None, strip white space
    if stripWhat == None:
    
        # sub white space at beginning
        beginningSpaceRegex = re.compile(r'^\s*')
        stripped = beginningSpaceRegex.sub("", toStrip)
        # sub white space at end
        endSpaceRegex = re.compile(r'\s*$')
        stripped = endSpaceRegex.sub("", stripped)

        return stripped

    # else, strip second argument
    else: 
        # convert stripWhat to string
        stripWhat = str(stripWhat)
        
        # add that to a valid regex
        myRegex = '^' + "(" + stripWhat + ")" + '*'
        print(f'myREgex: {myRegex}')

        # sub stripWhat at beginning
        beginningSpaceRegex = re.compile(myRegex)
        stripped = beginningSpaceRegex.sub("", toStrip)
        # sub stripWhat at end
        myRegex2 = "(" + stripWhat + ")" + '*' + '$'
        print(f'myregex2: {myRegex2}')
        endSpaceRegex = re.compile(myRegex2)
        stripped = endSpaceRegex.sub("", stripped)

        return stripped

question = "3 3 3 Write a function that takes a string and does the same thing as the strip() string3 3 3 3 "

print('WORKED___' +regexStrip(question, stripWhat = '3 ') + '___WORKED')