#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest
import magic


def main():

    # per http://stackoverflow.com/questions/43580/how-to-find-the-mime-type-of-a-file-in-python
    
    files = [
        './parse_excel/excel.xlsx',
        './callback.py',
    ]

    for x in files:
        mime = magic.Magic(mime=True)
        print(mime.from_file(x))


def test():
    pass


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
