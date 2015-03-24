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

def do_something(byte):
    with open('output2.txt', 'ab') as f:       # open as binary
        line = byte.decode('cp932', 'replace') # decode bytes using cp932
        # do something with line here
        byte = line.encode('utf-8', 'strict')  # encode string as utf8
        f.write(byte)                          # write it as bytes, which is actually utf8

line = b''  # empty bytearray
with open(myfile, 'rb') as f:
    while True:
        byte = f.read(1)
        line = line + byte

        if not byte:
            if line != b'':
                do_something(line)
            break

        if ord(byte)==10:
            do_something(line)
            line = b''
