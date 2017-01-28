#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest
import sys

try:
    sys.path.append(r'C:\code\text_filter')
    import text_filter
    print(r'path C:\code\text_filter exists!')
except ImportError:
    try:
        sys.path.append(r'~/dev/learning_python/')
        import text_filter
        print('path ~/dev/learning_python/ exists!')
    except ImportError:
        raise


def main():
    pass


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

