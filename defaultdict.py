#! /usr/bin/env python3

# https://docs.python.org/3/library/collections.html#collections.defaultdict
# variable = collections.defaultdict( default_factory )

import collections

warehouse = collections.defaultdict(int)
# initialize warehouse dict
# if a new key is given, create an entry with an empty list

list = [
    ('finished_good', 300),
    ('materials',     500),
    ('packaging',     2000),
    ('materials',     200),
    ('returns',       350),
    ('finished_good', 700),
]

for wh, qty in list:
    warehouse[wh] += qty

print(warehouse)
# defaultdict(<class 'int'>, {'packaging': 2000, 'materials': 700, 'finished_good': 1000, 'returns': 350})
