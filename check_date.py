#! /usr/bin/env python3

import datetime
import re
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
    if tmp is None or tmp == '':
        logging.debug('returning None.')
        return None
    elif type(tmp).__name__ == datetime.date.__name__:
        logging.debug('it\'s already a ' + type(tmp).__name__ + ' instance.')
        return tmp
    else:
        try:
            x = re.search('^(\d\d\d\d).(\d\d).(\d\d)$', tmp)
            return datetime.date(int(x.group(1)), int(x.group(2)), int(x.group(3)))
        except:
            try:
                x = re.search('^(\d\d).(\d\d).(\d\d\d\d)$', tmp)
                return datetime.date(int(x.group(3)), int(x.group(1)), int(x.group(2)))
            except:
                try:
                    x = re.search('^(\d\d).(\d\d).(\d\d)$', tmp)
                    return datetime.date(2000+int(x.group(3)), int(x.group(1)), int(x.group(2)))
                except:
                    logging.debug('"' + tmp + '" met no conditions stated. Falling back to None.')
                    return None

# tmp = check_date('02/14/15')
tmp = datetime.date(2015,2,13)
tmp = check_date(tmp)
print(tmp.isoformat())

