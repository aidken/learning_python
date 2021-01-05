#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys, io
import xlrd
from dataclasses import dataclass, field

# cSpell:ignore xlrd nrows datefmt


@dataclass
class Report:
    file: str
    records: list = field(default_factory=list, init=False)

    def __post_init__(self):
        pass


@dataclass
class Record:
    row_number: str

    def __post_init__(self):
        self.row_number = str(self.row_number).strip()


def parse(file, worksheet, row_of_label, callback=None):

    # iterate through rows of an Excel spreadsheet

    if callback is not None and not callable(callback):
        raise ValueError('callback given but it it not callable. It is a {}.'.format(
            type(callback)
        ))

    wb = xlrd.open_workbook(filename=file)
    ws = wb.sheet_by_name(worksheet)

    r = Report(file=file)

    for i in range(1, ws.nrows):
        # In xlrd, cell address is 1 based, not zero based
        # skip row 0, which is a label row. Assumption is you can ignore Excel row 1.

        x = Record(
            excel_row=i + 1,  # in xlrd, cell address is zero based.
            mode=ws.cell(i, 0).value,
        )

        if callback is not None and callable(callback):
            callback(x)
        else:
            r.records.append(x)

    if callback is None:
        return r


def main():
    pass


if __name__ == '__main__':

    # https://qiita.com/jack-low/items/91bf9b5342965352cbeb
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # logger setup
    filename = str(sys.argv[0])[:-3] + '.log'
    format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)-8s: %(message)s'
    logging.basicConfig(
        filename=filename,
        format  =format,
        datefmt ='%m-%d %H:%M',
        level   =logging.INFO,
        # level   =logging.DEBUG,
        # level   =logging.ERROR,
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
