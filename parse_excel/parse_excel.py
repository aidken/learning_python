#! /usr/bin/env python3

import os.path
import xlrd
import xlsxwriter
import datetime

excel_file = './excel.xlsx'
if not os.path.isfile(excel_file):
  quit()

wb = xlrd.open_workbook(excel_file)

for s in wb.sheets():
  print('Sheet: ' + s.name)
  for r in range(s.nrows):
    values = []
    for c in range(s.ncols):
      values.append('r=' + str(r) + ', c=' + str(c) + ': ' + s.cell(r,c).value)
    print('\t'.join(values))
  print()

# Excel row 1 is row 0 in python
# Excel col 1 is col 0 in python

new_wb = xlsxwriter.Workbook('./new_excel.xls')
new_ws = new_wb.add_worksheet('New Sheet')
format1 = new_wb.add_format({'num_format': '#,###.00'})
format2 = new_wb.add_format({'num_format': 'YYYY-MM-DD'})

new_ws.write( 0, 0, 123.45, format1)
new_ws.write( 1, 0, datetime.datetime.now().date(), format2)
new_ws.write( 0, 2, 10 )
new_ws.write( 1, 2, 25 )
new_ws.write( 2, 2, "=SUM(C1:C2)")
new_wb.close()                     # save and then close
