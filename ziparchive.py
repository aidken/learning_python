#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import io
import pytest
import zipfile
import datetime
import os.path


def main():

    # cf:
    # https://pymotw.com/3/zipfile/#appending-to-files

    # create a new text file
    now = datetime.datetime.now()
    now = now.strftime('%Y-%m-%d=%H-%M-%S')

    file_name = now + '.txt'
    with io.open(file_name, mode='w', encoding='utf-8') as output:
        output.write(now + '\n')

    # create zip archive if it's not there
    zip_archive = './test.zip'
    if not os.path.isfile(zip_archive):
        # create a new archive with mode='w'
        with zipfile.ZipFile(zip_archive, mode='w') as zf:
            zf.write(file_name)

    else:
        # append a file to an existing archive with mode='a'
        with zipfile.ZipFile(zip_archive, mode='a') as zf:
            zf.write(file_name)


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
