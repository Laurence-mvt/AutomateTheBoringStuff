def spam():
    bacon()

def bacon():
    raise Exception('This is the error message.')

spam()

# the above returns:
"""Traceback (most recent call last):
  File "/Users/laurencefinch/Desktop/.../errorExample.py", line 7, in <module>
    spam()
  File "/Users/laurencefinch/Desktop/.../errorExample.py", line 2, in spam
    bacon()
  File "/Users/laurencefinch/Desktop/.../errorExample.py", line 5, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message."""

# can get traceback as a string when you want exception handling in addition to traceback message
# can write traceback message to a new text file
# also see 'Logging' to use the logging module for similar, but better approach.

