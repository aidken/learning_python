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
    format   = '%(asctime)s: %(message)s',
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

def try_decode(line):
    try:
        line = line.decode('cp932', 'strict')  # decode bytes using cp932
        # do something with line here
    except UnicodeDecodeError:
        return True
    except:
        raise
    else:
        return False

mojibake_lines = []

line_count = 1
line       = b''  # empty bytearray
with open(myfile, 'rb') as f:
    while True:
        byte = f.read(1)
        line = line + byte

        # variable byte is not byte at the end of file
        if not byte:
            if line != b'':
                if try_decode(line):
                    mojibake_lines.append(line_count)
            line_count += 1
            break

        # when linefeed 0A is seen, it's the end of a line
        if ord(byte)==10:
            if try_decode(line):
                mojibake_lines.append(line_count)
            line_count += 1
            line = b''

if mojibake_lines:
    print('mojibake found at following line(s):')
    for x in mojibake_lines:
        print('line ' + str(x))
