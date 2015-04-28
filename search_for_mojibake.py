#! /usr/bin/env python3

# a first python script
import sys
import os.path
import logging

# logger setup
logfile = './log.txt'
logging.basicConfig(
    filename = logfile,
    format   = '%(asctime)s: %(message)s',
    level    = logging.DEBUG
)

def try_decode(line, encoding):
    try:
        line = line.decode(encoding, 'strict')  # decode bytes using cp932
        # do something with line here
    except UnicodeDecodeError:
        return True
    except:
        raise
    else:
        return False

def search_for_mojibake(myfile, encoding):

    # # see if myfile really exists
    # if not os.path.isfile(myfile):
    #     logging.critical("Cannot find file 'myfile'.")
    #     quit() # alternative sys.exit()

    # try:
    #     f = open(myfile, 'rb')
    # except FileNotFoundError:
    #     raise FileNotFoundError(str(myfile) + ' does not exist.')
    #     quit()
    # else:
    #     f.close()

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
                    if try_decode(line, encoding):
                        mojibake_lines.append(line_count)
                line_count += 1
                break

            # when linefeed 0A is seen, it's the end of a line
            if ord(byte)==10:
                if try_decode(line, encoding):
                    mojibake_lines.append(line_count)
                line_count += 1
                line = b''

            # if mojibake_lines:
            #     print('mojibake found at following line(s):')
            #     for x in mojibake_lines:
            #         print('line ' + str(x))

    return mojibake_lines
