#! /usr/bin/env python3

fruits = [
    'apple',
    'peach',
    'orange',
]

for i, fruit in enumerate(fruits, 1): # counter starts at 1
    print('{:03d}: {}'.format(i, fruit))
