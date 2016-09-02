#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys


def main():
    # logger setup
    logfile = str(sys.argv[0]) + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

    def test(x):
        print('x is {}.'.format(x))
        def test2():
            nonlocal x  # this enables modification to var x in the enclosing scope
            x += 1      # count up x
            return x
        return test2

    tmp = test(10)
    for i in range(20): print(tmp())

# ref: http://stackoverflow.com/questions/1261875/python-nonlocal-statement
# ref: http://stackoverflow.com/questions/4020419/why-arent-python-nested-functions-called-closures


if __name__=='__main__':
    main()

