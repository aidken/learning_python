#! /usr/bin/env python3

data = [(1,2), (2,3), (3,4)]

def test(cb):
  for x in data:
    print(cb(x[0], x[1]))

def callback(a, b):
  return a+b

test(callback)
