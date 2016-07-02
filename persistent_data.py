#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import os.path

storage = 'test.pickle'

if os.path.isfile(storage):
    print('{} exists. retrieving data.'.format(storage))
    tmp = pickle.load( open( 'test.pickle', 'rb' ) )
else:
    print('{} does not exist. creating data.'.format(storage))
    tmp = {
        'x': 123,
        'y': 456,
    }

    pickle.dump(
        tmp,
        open( 'test.pickle', 'wb' )
    )

for x in tmp:
    print('{} = {}'.format(x, tmp[x]))


