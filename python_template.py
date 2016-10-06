#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest

def main():
    # logger setup
    logfile = str(sys.argv[0]) + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

def test():


if __name__=='__main__':
    main()

