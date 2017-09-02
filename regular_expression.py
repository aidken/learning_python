#! /usr/bin/env python3

import re

def remove_zeros(var):
    try:
        m = re.match('^(\d+)\.00$', str(var))
        return m.group(1)
    # trap error in case match did not work
    except AttributeError:
        return var


def main():

    pieces = [
        '1.00',
        2.00,
        3,
        400
    ]

    # list comprehension
    pieces = [remove_zeros(x) for x in pieces]

    print(pieces)


    another_example = 'text_file.txt'

    print(re.sub('\.txt$', '.xlsx', another_example))
    # 'text_file.xlsx'

    print(re.sub('\.[a-zA-Z]+$', '.xlsx', another_example))
    # using character class, same result 'text_file.xlsx'

main()
