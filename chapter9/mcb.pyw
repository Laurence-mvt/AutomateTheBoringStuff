#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - Deletes keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
# if user wants to save copied content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()  # keyword saved as second command line argument, copied text saved for that keyword

# List keywords and load content.
# if user wants to see keywords
elif len(sys.argv) == 2 and sys.argv[1] == 'list':
    pyperclip.copy(str(list(mcbShelf.keys())))
# if user wants to copy keyword
elif len(sys.argv) == 2 and sys.argv[1] in mcbShelf.keys():
    pyperclip.copy(mcbShelf[sys.argv[1]])
# User wants to delete a keyword
elif len(sys.argv) == 3 and sys.argv[1] == 'delete' and sys.argv[2] in mcbShelf.keys():
    del mcbShelf[sys.argv[2]]
# User wants to delete all keywords
elif len(sys.argv) == 2 and sys.argv[1] == 'deleteAll':
    for key in mcbShelf.keys():
        del mcbShelf[key]

mcbShelf.close()


