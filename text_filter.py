#! /usr/bin/env python3

# a first python script
import sys
import re
import logging

def main():

    # logger setup
    logfile = str(sys.argv[0]) + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )


    # receive argument from command line
    try:
        myfile = sys.argv[1]                 # sys.argv is a list
        logging.debug("Filter starting on " + myfile)
    except IndexError:
        logging.error('Argument seems not passed.')
        raise

    try:
        with open(myfile, encoding='cp932') as tmp: # context manager
            for row_counter, line in enumerate(tmp, 1):
                # let's suppress all comments
                line = line.rstrip('\n')         # remove trailing newline
                line = re.sub('#.+', '', line)   # substitute anything after # with nothing
                print(line)
    except FileNotFoundError:
        logging.error('given file ' + myfile + ' is not found.')
        raise


if __name__=='__main__':
    main()
