#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import io
import datetime
from dataclasses import dataclass, field
import json

# cSpell:ignore datefmt encodable

class Order_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Order):

            # date_created = ''
            if isinstance(obj.date_created, datetime.date):
                date_created = obj.date_created.isoformat()
            elif obj.date_created == '':
                date_created = ''
            else:
                raise ValueError

            return {
                'item_number' : obj.item_number,
                'qty'         : obj.qty,
                'value'       : obj.value,
                'date_created': date_created,
                'container'   : obj.container,
            }
        else:
            return super().default(obj)


def Order_decoder(tmp):
    return Order(
        item_number  = tmp['item_number'],
        qty          = tmp['qty'],
        value        = tmp['value'],
        date_created = tmp['date_created'],
        container    = tmp['container'],
    )


def _convert_to_date(tmp) -> datetime.date:
    if tmp is None or tmp in ('None', ''):
        return ''
    elif isinstance(tmp, (datetime.date, datetime.datetime)):
        return datetime.date(
            year  = tmp.year,
            month = tmp.month,
            day   = tmp.day,
        )
    elif isinstance(tmp, str):
        x = datetime.datetime.strptime(tmp, '%Y-%m-%d')
        return datetime.date(
            year  = x.year,
            month = x.month,
            day   = x.day,
        )
    else:
        raise ValueError


def _convert_to_str(tmp) -> str:
    if tmp is None or tmp in ('None', ''):
        return ''
    else:
        return str(tmp).strip()


def _convert_to_int(tmp) -> int:
    if tmp is None or tmp in ('None', ''):
        return 0
    else:
        return int(tmp)


def _convert_to_float(tmp) -> float:
    if tmp is None or tmp in ('None', ''):
        return 0
    else:
        return float(tmp)


@dataclass
class Order():
    item_number : str
    qty         : int
    value : float
    date_created: datetime.date
    container   : str = ''

    def __post_init__(self):
        self.item_number  = _convert_to_str(self.item_number)
        self.qty          = _convert_to_int(self.qty)
        self.value        = _convert_to_float(self.value)
        self.date_created = _convert_to_date(self.date_created)
        if self.container is None or self.container == 'None':
            self.container = ''


def main():
    l = list()

    l.append( Order(
        item_number  = 'Pencil',
        qty          = 1008,
        value        = None,
        date_created = datetime.date(2021, 5, 1),
        container    = None,
    ) )

    l.append( Order(
        item_number  = 'Eraser',
        qty          = 1100,
        value        = 1100 * 0.79,
        date_created = None,
        container    = 'ABC1234567',
    ) )

    for x in l:

        print(type(x))
        tmp = json.dumps(x, cls=Order_encoder)

        print(tmp)
        y = json.loads(tmp, object_hook=Order_decoder)

        print(y)


if __name__ == '__main__':

    # https://qiita.com/jack-low/items/91bf9b5342965352cbeb
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # logger setup
    filename = str(sys.argv[0])[:-3] + '.log'
    format = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)-8s: %(message)s'
    logging.basicConfig(
        filename = filename,
        format   = format,
        datefmt  = '%m-%d %H:%M',
        level    = logging.INFO,
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
