#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest


def items():
    return {
        'A': 'food',
        'B': 'liquar',
        'C': 'food',
        'D': 'cosmetics',
        'E': 'liquar',
        'F': 'food',
    }

def category_sort_order():
    return {
        'food':      100,
        'cosmetics': 200,
        'liquar':    300,
        'unknown':   999,
    }

def return_sort_logic():

    items_db               = items()
    category_sort_order_db = category_sort_order()

    # create a sort helper that refers to data outside its local scope
    def sort_logic(item_number):

        try:
            category = category_sort_order_db[items_db[item_number]]
        except IndexError:
            category = 'unknown'

        return (category, item_number)

    return sort_logic


def main():

    sl = return_sort_logic()

    items = [
        'D',
        'B',
        'C',
        'A',
        'B',
        'E',
        'F',
        'E',
    ]

    print(
        # [i for i in sorted(items, key=lambda x: sl(x))]
        [i for i in sorted(items, key=sl)]
    )


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
