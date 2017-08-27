#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
from io   import StringIO
import tmp


def main():
    stream1 = StringIO('Here is sample text!\nDo something to me!\n')
    tmp.main(stream1)

    with open('./tmp.py', 'r', encoding='utf-8') as stream2:
        tmp.main(stream2)


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
