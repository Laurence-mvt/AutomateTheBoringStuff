# chapter 10: Organizing files notes

import shutil, os
from pathlib import Path

# copy files
p = Path.cwd()
# shutil.copy(p/'AutomateTheBoringStuff/chapter10/notes.py', p/'AutomateTheBoringStuff/chapter9') # copies notes.py file to chapter9 folder

# copy a folder (tree) 
# shutil.copytree(p/'AutomateTheBoringStuff/chapter10', p/'AutomateTheBoringStuff/chapter10Copy')

# move a file
# shutil.move('source', 'destination')

# delete single file at 'path'
# os.unlink('path') 

# delete empty folder at 'path'
# os.rmdir('path')

# delete a folder at 'path' and all files and folders it contains 
# shutil.rmtree('path')

# when deleting files/folders, good practice to run script for first time replacing 
# delete method with print(files to be deleted) in its place

# instead of doing permanent delete with above, can use send2trash, for safer, soft delete (i.e. send to trash/recycle bin) - RECOMMENDED
"""import send2trash
baconFile = open('bacon.txt', 'a') # created the file
baconFile.write('Bacon is not a veg')
baconFile.close()
send2trash.send2trash('bacon.txt')"""

"""# get at the tree of the current directory with os.walk()
for folderName, subfolders, filenames in os.walk(Path.cwd()):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF' + folderName + ': ' + subfolder)

    for filename in filenames:
            print('FILE INSIDE ' + folderName + ': ' + filename)"""

# to work with zip files
import zipfile, os
from pathlib import Path
p = Path.cwd()/'AutomateTheBoringStuff'/'chapter10'
exampleZip = zipfile.ZipFile(p/'example.zip')   
exampleZip.namelist() # list of strings for all files and folders contained. ['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('spam.txt')
spamInfo.file_size
spamInfo.compress_size
print(f'Compressed file is {round(spamInfo.file_size/spamInfo.compress_size,2)}x smaller!')
exampleZip.close()

# extract from zip file
p = Path.cwd()/'AutomateTheBoringStuff'/'chapter10'
exampleZip = zipfile.ZipFile(p/'example.zip')
exampleZip.extract('specificFileOrFolder.filetype', 'destination') # to extract specific file/folder
exampleZip.extractall()     # to extract entire zip file, optional argument to set which folder to extract to
exampleZip.close()

# create a zip file
newZip = zipfile.ZipFile('new.zip', 'w') # open in write mode
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED) # can use other compression type parameters, but ZIP_DEFLATED works well for all data types



