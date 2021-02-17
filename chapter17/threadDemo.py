import threading, time
print('Start of program.')

def takeANap():
    time.sleep(5)
    print('Wake up!')

threadObj = threading.Thread(target=takeANap)   # creates the Thread object
threadObj.start()   # creates the new thread and starts executing takeANap() function

print('End of program')

# Python program will only terminate once all threads have terminated

# to pass in arguments to the target function
threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'], kwargs={'sep':' & '})
threadObj.start()