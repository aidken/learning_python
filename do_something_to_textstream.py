#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys

def main(stream):
    print(type(stream))
    print()

    for x in stream:
        print("This part is added by main(): " + x)

    print()


if __name__=='__main__':

    # logger setup
    logfile = str(sys.argv[0])[:-3] + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

    main()
