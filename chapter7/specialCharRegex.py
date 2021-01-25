import re

# the pipe '|' character signifies 'or' 
batRegex = re.compile(r'Bat(mobile|man|life)')

mo = batRegex.search("nenenenenenene... Batman!!")

print(mo.group())
print(mo.group(1))

# the question mark '?' character signifies the preceding group is optional, e.g.:
batRegex = re.compile(r'Bat(wo)?man')

mo = batRegex.search('the adventures of Batman')
print(f'Batman: {mo.group()}')

mo = batRegex.search('the adventures of Batwoman')
print(f'Batwoman: {mo.group()}')

# the asterix '*' character means match 0 or more of the preceding group, e.g.:
batRegex = re.compile(r'Bat(wo)*man')

mo = batRegex.search('Batwowowowoman')
print(mo.group()) # = 'Batwowowowoman'

# the plus '+' character means match one or more of the preceding group, e.g.:
batRegex = re.compile(f'Bat(wo)+man')

mo = batRegex.search('the adventures of Batwoman') 
print(mo.group()) # = 'Batwoman'
mo = batRegex.search('the adventures of Batman') 
print(mo == None) # True

# match specific number of repititions with {x}, e.g.:
haRegex = re.compile(r'(ha){3}')

mo = haRegex.search('hahaha') # hahaha
print(mo.group())
mo = haRegex.search('haha') # NoneType

# specify range of repititions with {x, y}, e.g.:
haRegex = re.compile(r'(ha){2,7}')

mo = haRegex.search('hahahahahahaha') 
print(mo.group()) 

# regular expressions are greedy by default, meaning that they return the longest string possible
# to specify them as lazy, meaning returning the minimum length string possible, use question mark, at the end of the {x,y}

# use findall() method, to return ALL instances of matched regexes, unlike search() which returns only the first match
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # ['415-555-9999', '212-555-0000']

# when the regex has groups, findall() returns a list of tuples
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000') # [('415', '555', '9999'), ('212', '555', '0000')]

# can make your own character class using [xxxx]:
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
for vowel in mo:
    print(vowel, end="") # oooeaaooAOO(base)

# can include a range of characters, when separated by a hyphen, e.g.:
letNumLowUpperRegex = re.compile(r'[a-zA-Z0-9]')
mo = letNumLowUpperRegex.findall('faslkfasdkghas798 9987hf ahf')
for character in mo:
    print(character, end="") # oooeaaooAOOfaslkfasdkghas7989987hfahf(base)
print()

# specify character to not be matched, and return all others using ^
consonantRegex = re.compile(r'[^aeiouAEIOU]')
consonantRegex.findall('RoboCop eats baby food. BABY FOOD.') # ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', '', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

# use ^ at beginning of regex to indicate that a match must occur at the beginning of the searched text. 
beginsWithHello = re.compile(r'^Hello')
beginsWithHello.search('Hello, world') # <re.Match object; span=(0, 5), match='Hello'>

# use $ at end of regex to indicate that match must occur at end of the searched text:
endsWithNumber = re.compile(r'\d$')
endsWithNumber.search('your number is 42') # <re.Match object; span=(16, 17), match='2'>
endsWithNumber.search('your number is forty two') == None # True

# use . character as wildcard that matches with any character, except for a newline
atRegex = re.compile(r'.at')
atRegex.findall('The cat in the hat sat on the flat mat.') # ['cat', 'hat', 'sat', 'lat', 'mat']

# use dot-star (.*)  to match with anything
nameRegex = re.compile(r'Firstname: (.*)Lastname: (.*)')
mo = nameRegex.search('Firstname: Laurence Lastname: Finch')
print(mo.group()) # Firstname: Laurence Lastname: Finch
mo.group(1) # Laurence
mo.group(2) # Finch

# dot-star uses greedy mode
# use (.*?) to specify lazy mode

# to make dot star recognise the newline character, use re.DOTALL as second re.compile argument:
noNewlineRegex = re.compile(r'.*')
mo = noNewlineRegex.search('this is first line\nthis is second line\nthis is third line')
print(mo.group()) # 'this is first line'

noNewlineRegex = re.compile(r'.*', re.DOTALL)
mo = noNewlineRegex.search('this is first line\nthis is second line\nthis is third line')
print(mo.group())# 'this is first line\nthis is second line\nthis is third line'

# ignore case by passing re.IGNORECASE or re.I as second argument to re.compile()
tedRegex = re.compile(r'ted', re.I)
mo1 = tedRegex.search('Ted') # Ted
mo2 = tedRegex.search('TED') # TED
print(mo1.group())
print(mo2.group())

# can substitute strings into regexp with sub() method
subRegex = re.compile(r'Agent \w+')
subbed = subRegex.sub('CENSORED', 'Agent Alice is sleeping with Agent Bob')
print(subbed)

# can substitute matched groups back into subbed output, using \1, \2, \3, ... to represent the group of text 1, 2, 3,...
subRegex = re.compile(r'Agent (\w)(\w*)')
subbed = subRegex.sub(r'\1****', 'Agent Alice is sleeping with Agent Bill, and Agent Chris knows about it and plans to tell Agent Dave')
print(subbed)

# can use re.VERBOSE mode to make complex regex more readable by ignoring whitespace and comments, e.g.:
phoneRegex = re.compile(r'''( 
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE) # note use of '''''' to allow for white space

# combine re.IGNORECASE and re.VERBOSE (and other optional arguments) with the pipe '|' operator (here meaning 'and')
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)