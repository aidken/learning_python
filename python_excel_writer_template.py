#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys

'''
Python template for creating an Excel file.
https://xlsxwriter.readthedocs.io/
'''

def main():

    # logger setup
    logfile = str(sys.argv[0]) + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

    wb_name = 'tmp.xlsx'
    ws_name = 'Sheet1'

    import xlsxwriter
    wb = xlsxwriter.Workbook(wb_name)
    ws = wb.add_worksheet(ws_name)

    # freeze panes
    ws.freeze_panes(3,15)

    # define excell cell formats
    # color codes here: http://www.rapidtables.com/web/color/RGB_Color.htm
    format_def = wb.add_format({
        'num_format': u'#,###;[Red]-#,###;;@',
        'font_name':  'Arial',
        'font_size':  9,
        'font_color': '#000000',
    })
    format_int   = wb.add_format({'num_format': '#,###'})
    format_yen   = wb.add_format({
        'font_name':  'Arial Narrow',
        'num_format': u'#,##0 円;[Red]-#,##0 円;;',
        'font_size':  9,
        'font_color': 'gray',
    })
    format_date_jpn = wb.add_format({
        'num_format': u'[$-409]M月D日',
        'font_name':  'Arial',
        'font_size':  9,
    })
    format_month = wb.add_format({
        'num_format': '[$-409]MMM YYYY',
        'font_name':  'Arial',
        'font_size':  9,
        'font_color':  '#1E90FF',
        'bold':       True,
        'bg_color': '#b0e0e6',
    })

    row = 0    # row base 0
    col = 0    # col base 0

    ws.write(row, col, u'Hello from Python!', format_def )

    # hide a column
    ws.set_column(  0,  0, None, None, {'level': 1, 'hidden': True} ) # A

    wb.close()


if __name__=='__main__':
    main()
