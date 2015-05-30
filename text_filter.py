#! /usr/bin/env python3

# a first python script
import sys
# import os.path
import re
import logging

# logger setup
logfile = './log'
logging.basicConfig(
    filename = logfile,
    format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
    level    = logging.DEBUG
)

# receive argument from command line
try:
    myfile = sys.argv[1]                 # sys.argv is a list
    logging.debug("Filter starting on " + myfile)
except IndexError:
    logging.critical('Argument seems not passed.')
    raise

# sys.argv[0] is always the name of this very program

# see if myfile really exists
# if not os.path.isfile(myfile):
#     logging.critical("Cannot find file 'myfile'.")
#     quit()                             # alternative sys.exit()

try:
    with open(myfile, encoding='cp932') as tmp: # context manager
        for line in tmp:                   # don't forget colon at the end.
            # let's suppress all comments
            line = line.rstrip('\n')         # remove trailing newline
            line = re.sub('#.+', '', line)   # substitute anything after # with nothing
            print(line)
except FileNotFoundError:
    logging.critical('given file ' + myfile + ' is not found.')
    raise
