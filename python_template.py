#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io
import logging
import argparse

# cSpell:ignore datefmt levelname

# get logger of this library __name__ and attach a null handler
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def main():
    arg_parser = argparse.ArgumentParser()
    group = arg_parser.add_mutually_exclusive_group()

    group.add_argument("-a", "--aaa", action="store_true", help="Do AAA.")
    group.add_argument("-b", "--bbb", action="store_true", help="Do BBB.")
    group.add_argument("-c", "--ccc", action="store_true", help="Do CCC.")
    group.add_argument("-d", "--ddd", action="store_true", help="Do DDD.")

    args = arg_parser.parse_args()

    # if no argument is passed, show help
    if len(sys.argv) == 1:
        arg_parser.print_help(sys.stderr)
        sys.exit(1)

    elif args.aaa:
        aaa()
    elif args.bbb:
        bbb()
    elif args.ccc:
        ccc()
    elif args.ddd:
        ddd()
    else:
        arg_parser.print_help()


def aaa():
    logger.info("This is INFO, inside function aaa().")
    logger.debug("This is DEBUG, inside function aaa().")
    logger.warning("This is WARNING, inside function aaa().")
    logger.error("This is ERROR, inside function aaa().")


def bbb():
    pass


def ccc():
    pass


def ddd():
    pass


if __name__ == "__main__":

    # https://qiita.com/jack-low/items/91bf9b5342965352cbeb
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    # logger setup:
    # if this library is run as a script, these logger setup is used
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_name = str(sys.argv[0])[:-3] + ".log"
    handler_file = logging.FileHandler(file_name)
    handler_file.setLevel(logging.DEBUG)
    formatter_file = logging.Formatter(
        "%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s"
    )
    handler_file.setFormatter(formatter_file)
    logger.addHandler(handler_file)

    # console logger to show INFO messages
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.INFO)
    formatter_console = logging.Formatter("%(name)s: %(levelname)s %(message)s")
    handler_console.setFormatter(formatter_console)
    logger.addHandler(handler_console)

    main()
