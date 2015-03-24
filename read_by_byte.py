#! /usr/bin/env python3

# a first python script
import sys
import os.path
import re
import logging

# logger setup
logfile = './log.txt'
logging.basicConfig(
    filename = logfile,
    level    = logging.DEBUG
)
# receive argument from command line
myfile = sys.argv[1] # sys.argv is a list
logging.debug("Filter starting on " + myfile)

# sys.argv[0] is always the name of this very program
# see if myfile really exists
if not os.path.isfile(myfile):
    logging.critical("Cannot find file 'myfile'.")
    quit() # alternative sys.exit()

line = b''  # empty bytearray
with open(myfile, 'rb') as f, open('output.txt', 'wb') as new_file:
    while True:
        byte = f.read(1)
        line = line + byte

        if not byte:
            if line != b'':
                new_file.write(line)
            break

        # if it's linefeed, add it twice
        if ord(byte)==10:
            line = line + byte
            new_file.write(line)
            line = b''
