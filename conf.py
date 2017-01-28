#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('tmp.conf')

    print(config)

    print(type(config))                # <class 'configparser.ConfigParser'>

    # mutate value
    print(config['TEST']['this'])
    # config['TEST']['this'] = 1000    # error. value must be string.
    config['TEST']['this'] = '1000'
    print(config['TEST']['this'])


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
