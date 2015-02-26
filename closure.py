#! /usr/bin/env python3

def create_closure(l):
  def tmp(x):
    return [ i + x for i in l ]
  return tmp

test = create_closure([2,3,4])
for i in test(5):
  print(i)        # 7 8 9
