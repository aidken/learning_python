#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import os.path

storage = 'test.pickle'

if os.path.isfile(storage):
    tmp = pickle.load( open( 'test.pickle', 'wb' ) )
else:
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


