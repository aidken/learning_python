#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import shutil
from io import BytesIO, StringIO


def main():

    # cf. https://stackoverflow.com/questions/26879981/writing-then-reading-in-memory-bytes-bytesio-gives-a-blank-result
    myio = StringIO()

    tmp=[
        'Hi!',
        '',
        'Here is some text file!',
        'Line #4'
        ]

    with open('file.txt', 'w') as f:

        for x in tmp:
            myio.write(x)
            myio.write('\n')

        myio.seek(0)

        # cf. https://stackoverflow.com/questions/3253258/what-is-the-best-way-to-write-the-contents-of-a-stringio-to-a-file
        shutil.copyfileobj(myio, f)

    # What I want to do is to have an IO,
    # add data to it, and then create a file. Looks it works.


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
