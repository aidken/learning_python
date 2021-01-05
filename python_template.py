#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import io
import argparse

# cSpell:ignore datefmt


def main():
    arg_parser = argparse.ArgumentParser()
    group = arg_parser.add_mutually_exclusive_group()

    group.add_argument(
        '-a', '--aaaaa', action='store_true', help='Do AAAAA.'
    )
    group.add_argument(
        '-b', '--bbbbb', action='store_true', help='Do BBBBB.'
    )
    group.add_argument(
        '-c', '--ccccc', action='store_true', help='Do CCCCC.'
    )
    group.add_argument(
        '-d', '--ddddd', action='store_true', help='Do DDDDD.'
    )

    args = arg_parser.parse_args()

    if args.aaaaa == True:
        aaaaa()
    elif args.bbbbb == True:
        bbbbb()
    elif args.ccccc == True:
        ccccc()
    elif args.ddddd == True:
        ddddd()

def aaaaa():
    pass


def bbbbb():
    pass


def ccccc():
    pass


def ddddd():
    pass


if __name__ == '__main__':

    # https://qiita.com/jack-low/items/91bf9b5342965352cbeb
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # logger setup
    filename = str(sys.argv[0])[:-3] + '.log'
    format = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)-8s: %(message)s'
    logging.basicConfig(
        filename=filename,
        format=format,
        datefmt='%m-%d %H:%M',
        level=logging.INFO,
        # level    = logging.DEBUG,
        # level    = logging.ERROR,
    )

    # https://docs.python.org/3/howto/logging-cookbook.html#logging-to-multiple-destinations
    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    main()
