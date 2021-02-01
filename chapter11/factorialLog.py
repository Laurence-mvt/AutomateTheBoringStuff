#! python3

import logging

# logging.disable(logging.CRITICAL) # turn off logging 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n))
    total = 1 
    for i in range(1, n+1):
        total *=i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    print(f'total: {total}')
    return total

print(factorial(5))
logging.debug('End of program')

# logging is a useful way to track events when program runs. logging.debug prints messages to screen as program runs, 
# formatted in the way specified in logging.basicConfig

# using logging is preferable to using print statements, because you get more info, and can more easily  turn them off when done debugging (with the logging.disable function in line 5)

# use logging levels to track different severities of events/errors. Levels are DEBUG, INFO, WARNING, ERROR, CRITICAL
# edit the level='' in basicConfig function to only display messages of the chosen level and above

# write logging messages to a text file 
# logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format = '....')