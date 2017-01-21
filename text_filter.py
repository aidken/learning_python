#! /usr/bin/env python3

# my first python script
import sys
import re
import logging

def main():

    # receive argument from command line
    try:
        myfile = sys.argv[1]                 # sys.argv is a list
        logging.debug('Filter starting on {}'.format(myfile))
    except IndexError:
        logging.exception('Argument not passed.')
        raise

    try:
        with open(myfile, encoding='cp932') as tmp: # context manager
            for row_counter, line in enumerate(tmp, 1):
                # let's suppress all comments
                line = line.rstrip('\n')         # remove trailing newline
                line = re.sub('#.+', '', line)   # substitute anything after # with nothing
                print(line)
    except FileNotFoundError:
        logging.exception('Given file {} is not found.'.format(myfile))
        raise


if __name__=='__main__':

    # logger setup
    logfile = str(sys.argv[0]) + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

main()
