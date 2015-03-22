#! /usr/bin/env python3

import json

tmp = {
        'product a': {
                       'desc':  'foo',
                       'sales': [123,127,130],
        },
        'product b': {
                       'desc':  'bar',
                       'sales': [234,230,270],
        },
}

tmp = {

print(json.dumps(tmp, indent=4))
