#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, io
import logging
import csv
from dataclasses import dataclass, field

# cSpell:ignore datefmt


@dataclass
class Report:
    file: str
    records: list = field(default_factory=list, init=False)

    def __post_init__(self):
        pass


@dataclass
class Record:
    row_number: int

    def __post_init__(self):
        if not isinstance(self.row_number, int):
            self.row_number = int(str(self.row_number).strip())


def parse(file, callback=None):

    # iterate through rows of an Excel spreadsheet

    if callback is not None and not callable(callback):
        raise ValueError(
            f'callback given but it it not callable. It is a {type(callback)}.'
        )

    r        = Report(file=file)
    encoding = 'utf-8'

    with open(file=file, encoding=encoding) as csvfile:
        # with open(file=file, encoding=encoding, errors='surrogateescape') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='\t')
        for row_number, row in enumerate(csvreader, 1):

            if row_number <= 3:
                logging.debug(
                    f"Row {row_number}. First three rows are ignored. Skipping.")
                continue

            elif len(row) == 0:
                logging.debug(
                    f"Row {row_number}. Length of row is zero. Skipping.")
                continue

            x = Record(
                row_number=row_number,
            )

            # run callback at record that's just been created.
            # you may want to run callback after r report has been finalized.
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
