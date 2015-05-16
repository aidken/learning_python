#! /usr/bin/env python3

import re

def remove_zeros(var):
    try:
        m = re.match('^(\d+).00$', str(var))
        return m.group(1)
    # trap error in case match did not work
    except AttributeError:
        return var

pieces = ['1.00',2.00,3]

# list comprehension
pieces = [remove_zeros(x) for x in pieces]

print(pieces)
