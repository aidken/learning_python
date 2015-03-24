#! /usr/bin/env python3

import datetime
import logging

logfile = './log.txt'
logging.basicConfig(
    filename=logfile,
    level   =logging.DEBUG
)

def check_date(tmp):
    '''
    Check a given value, and convert it to a datetime.date object if possible.
    Return None if not possible
    '''
    logging.debug('check_date received ' + tmp)

    if type(tmp).__name__ == datetime.date.__name__:
        logging.debug('it\'s already a ' + type(tmp).__name__ + ' instance.')
        return tmp
    elif tmp == None or tmp == '' or type(tmp).__name__ != type('x').__name__:
        logging.debug('returning None.')
        return None
    else:
        try:
            x = datetime.datetime.strptime(tmp, "%Y-%m-%d")
            return x
        except ValueError:
            try:
                x = datetime.datetime.strptime(tmp, "%m-%d-%Y")
                return x
            except ValueError:
                try:
                    x = datetime.datetime.strptime(tmp, "%m-%d-%y")
                    return x
                except ValueError:
                    logging.debug('"' + tmp + '" met no conditions stated. Falling back to None.')
                    return None

tmp = check_date('02-14-15')
# tmp = check_date('2015-02-15')
print(tmp.strftime('%Y-%m-%d'))
