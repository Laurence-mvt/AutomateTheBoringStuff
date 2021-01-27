from pathlib import Path
# format paths supplied as suitable to the caller's device and OS (Windows, mac, Linux)

myPath = Path('spam', 'bacon', 'eggs')   # returns Path object PosixPath('spam/bacon/eggs') on mac/Linux, WindowsPath('spam/bacon/eggs') on Windows
# to get path as string
print(str(myPath)) # 'spam/bacon/eggs' on mac

# can join (concatenate) paths using '/' operator, as long as the first value is a Path object
print(Path('spam') / 'bacon' / 'eggs')
# this is safer than concatenating using '+', because '/' formats for the user's os automatically, unlike '+'

# get the current working directory for the program 
Path.cwd()

"""
# change cwd:
import os
os.chdir('newDirectoryHere')
"""

# get a Path object of home directory
Path.home()

"""
# make new directory (folder)
import os
os.makedirs('newDirectoryHere')

# will make many directories at once, if have multiple new folders in file path
os.makedirs('root/new1/new2/new3') # will make new1, new2, new3 folders

# make directory from a Path object (only one at a time, unlike os.makedirs())
Path('newDirectory').mkdir()      # will create new1 folder
"""

# check path is absolute path (and not relative)
Path.cwd().is_absolute() # True
Path('spam/eggs/bacon') # False

# to get absolute from relative, generally will put Path.cwd()/'relativePathHere', since most often we use paths relative to cwd

# get string of absolute path, to convert relative path to absolute
import os
os.path.abspath('relativePathHere')

# to get relative path from a path
os.path.relpath('start/path', 'start') # returns 'path'

# access the different parts (anchor, parent, name) 
p = Path('pathHere/parent/anotherparent/name')
p.anchor    # the root folder of the filestystem
p.parent    # the path object to the file 
p.stem      # the file name without extension (file type)
p.suffix    # the file extension (type)
p.name      # the file name + extension

# can get into ancestor folders of a Path object
print(p)           # pathHere/parent/name/anothername
print(p.parents)   # <PosixPath.parents> # a string list of ancestor folders
print(p.parents[0]) # pathHere/parent/anotherparent
print(p.parents[1]) # pathHere/parent
print(p.name)       # name

# get file size of the file in the path argument
ex = os.path.getsize(Path.cwd())
print(ex) # 256

# get files in path argument
ex = os.listdir(Path.cwd())
print(ex) # ['.DS_Store', 'automate_online-materials', '__pycache__', '.vscode', 'AutomateTheBoringStuff', '.idea']

# get total of file sizes in a directory
totalSize = 0
for filename in os.listdir(Path.cwd()):
    totalSize += os.path.getsize(os.path.join(Path.cwd(),filename))

print(totalSize) # 12964

# use glob() as way to get at files in a particular directory more convenients
p = Path.cwd()
p.glob('*') # returns generator object, * stands for all files in that directory
list(p.glob('*'))

# can treat glob argument as simplified regular expressions (* means multiple of an characters)
list(p.glob('*.text')) # to list all text files
# '?' stands for single character

for filePath in list(p.glob('*')):
    print(filePath)     # prints as string
    # do something with the file


# check path exists on the computer to avoid errors
t = Path.cwd().exists() # True
f = Path('fakePath').exists() # False
print(t)
print(f)

# note different file types (binary files), will have different libraries to work with them

# for plaintext files, pathlib module useful
p = Path('spam.txt')
p.write_text('Hello, world!') # creates (writes) a new text file and returns 13, i.e  the number of characters in that text file

# more commen, general steps for writing to a file
# 1. call the open() funciton to return a File object
helloFile = open(Path.cwd()/'spam.txt') # opens in read mode (i.e. can't edit/write to the file). (the default, but can make it explicit by adding 'r' as second argument)

# 2. call the read() or write() function on the File object
# reading files
helloFile.read() # 'Hello, world!'
helloFile.readlines() # returns list of lines in text file

# writing files, use 'w' as second argument, and 'a' for append mode
baconFile = open('bacon.txt', 'w')
baconFile.write('Hello,world!\n')   # will create new file if baconFile doesn't exist already
baconFile.close()
baconFile = open('bacon.txt', 'a')
baconFile.write('Bacon is great!') # baconFile now 'Hello, world!\nBacon is great!'
baconFile.close()

# 3. close the file by calling the close() method on the File object
# baconFile.close()
baconFile = open('bacon.txt', 'r')
print(baconFile.read())






