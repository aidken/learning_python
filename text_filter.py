#! /usr/bin/env python3

# a first python script
import sys
import os.path
import re

# receive argument from command line
myfile = sys.argv[1]                 # sys.argv is a list
print("myfile given is " + myfile)

# sys.argv[0] is always the name of this very program

# see if myfile really exists
if not os.path.isfile( myfile ):
  print("Cannot find file 'myfile'.")
  quit()                             # alternative sys.exit()

with open(myfile, encoding='cp932') as tmp: # context manager
  for line in tmp:                   # don't forget colon at the end.
    # let's suppress all comments
    line = line.rstrip()             # remove newline
    line = re.sub('#.+', '', line)   # substitute anything after # with nothing
    print(line)
