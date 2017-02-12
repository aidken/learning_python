#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest
import sample_class

# http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner
# http://stackoverflow.com/questions/13211535/correct-use-of-static-methods

def main():

    a='Hello!'
    b='World'
    c='2017-05-29'

    c=sample_class.one.date_from_string(c)

    x=sample_class.one(
        a=a,
        b=b,
        c=c,
    )

    print(x)


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
