#! /usr/bin/env python3

import sys
import os.path
import re
import decimal

# decimal.getcontext().prec = 2 # this is not what I wanted, not what it looks to do
                                # https://stackoverflow.com/questions/3877299/python-question-about-decimal-arithmetic

class Order:
  def __init__( self, orderNumber, shipToState, itemLines = [] ):
    self.orderNumber = orderNumber
    self.shipToState = shipToState
    self.itemLines   = itemLines
  def addItemLine( self, itemLine ):
    self.itemLines.append( itemLine )
    return self.itemLines[ -1 ]
  def orderAmount( self ):
    return sum( [ itemLine.subtotal for itemLine in self.itemLines ] )
  def itemLinesCount( self ):
    return len( self.itemLines )

class ItemLine:
  def __init__( self, itemNumber, qtyOrdered, subtotal ):
    self.itemNumber = itemNumber
    self.qtyOrdered = int(qtyOrdered)             # this is interger
    self.subtotal   = decimal.Decimal( subtotal ) # this is floating but let's use decimal.Decimal

def print_header():
  print( '\t'.join( [
                      'order_number',
                      'ship_to_state',
                      'item_lines_count',
                      'order_amount',
                      'item_number',
                      'qty_ordered',
                      'item_subtotal'
                    ] ) )

def print_order( order ):
  for itemLine in order.itemLines:
    print( '\t'.join( [
                        order.orderNumber,
                        order.shipToState,
                        str(order.itemLinesCount()),
                        str(order.orderAmount()),
                        itemLine.itemNumber,
                        str(itemLine.qtyOrdered),
                        str(itemLine.subtotal)
                      ] ) )         # join expects a list of str

myReport = sys.argv[1]
if not os.path.isfile( myReport ):
  print( "cannot find report 'myReport'." )
  quit()

print_header()

order = None

for line in open( myReport ):
  line  = line.rstrip()
  items = re.split( '\t', line )

  if re.match( '^\d+$', items[0] ): # if first item is numeral, it's order number
    if order != None:
      print_order( order )
    order = Order( items[0], items[1], [] )
  else:
    itemLine = ItemLine( items[0], items[1], items[2] )
    order.addItemLine( itemLine )

print_order( order )                # don't forget to print the last order
