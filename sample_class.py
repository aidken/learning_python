#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest
import datetime


class one():
    @staticmethod
    def date_from_string(date):
        # assumes argument date is in the format of 'yyyy-mm-dd'
        year, month, day = map(int, date.split('-'))
        return datetime.date(year, month, day)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c  # this should be datetime.date

    def __str__(self):
        return 'a={}, b={}, c={}'.format(
            self.a,
            self.b,
            self.c.isoformat(),
        )


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
