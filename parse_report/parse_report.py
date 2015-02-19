#! /usr/bin/env python3

import sys
import os.path
import re

myReport = sys.argv[ 1 ]
if not os.path.isfile( myReport ):
  print( "cannot find report 'myReport'.", end='\n' )
  quit()

orderNumber = 0;
shipToState = '';

for line in open( myReport ):
  line = line.rstrip()
  items = re.split( r'\t', line )     # what's this r in r'\t'? indicating re?

  if re.match( '^\d+$', items[ 0 ] ): # if first item is numeral, it's order number
    orderNumber = items[ 0 ]
    shipToState = items[ 1 ]
  else:
    itemNumber  = items[ 0 ]
    qtyOrdered  = items[ 1 ]
    subtotal    = items[ 2 ]

    print( '\t'.join( [ orderNumber, shipToState, itemNumber, qtyOrdered, subtotal ] ), end='\n' )
