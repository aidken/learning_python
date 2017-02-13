#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest
import datetime


def date_from_string(x):

    if x==None:
        return None

    else:
        try:
            x=datetime.datetime.strptime(x, '%Y-%m-%d')
            x=datetime.date(
                x.year,
                x.month,
                x.day
            )
            return x

        except:
            try:
                x=datetime.datetime.strptime(x, '%Y/%m/%d')
                x=datetime.date(
                    x.year,
                    x.month,
                    x.day
                )
                return x
            except:
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
