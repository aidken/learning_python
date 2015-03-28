#! /usr/bin/env python3

def create_closure(l):
  """
  create_closure(list) returns a function that receives a number as argument.
  The function adds that number you gave as argument to each element of the list, and return the list as result.

  To view this document, run this:
  >>> import create_closure
  >>> help(create_closure.create_closure)

  """
  def tmp(x):
    return [ i + x for i in l ]
  return tmp

test = create_closure([2,3,4])
for i in test(5):
  print(i)        # 7 8 9
