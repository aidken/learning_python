#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys

'''
Python template for creating an Excel file.
https://xlsxwriter.readthedocs.io/
'''

def main():

    wb_name = 'tmp.xlsx'
    ws_name = 'Sheet1'

    import xlsxwriter
    wb = xlsxwriter.Workbook(wb_name)
    ws = wb.add_worksheet(ws_name)

    # define excell cell formats
    # color codes here: http://www.rapidtables.com/web/color/RGB_Color.htm
    format_def = wb.add_format({
        'num_format': u'#,###;[Red]-#,###;;@',
        'font_name':  'Arial',
        'font_size':  9,
        'font_color': '#000000',
    })
    format_int   = wb.add_format({
        'num_format': '#,##0;[Red]-#,##0;;@',
        'font_name':  'Courier New',
        'font_size':  9,
    })
    format_pcs   = wb.add_format({
        'num_format': '#,##0 個;[Red]-#,##0 個;;@',
        'font_name':  'Courier New',
        'font_size':  9,
        'font_color': '#003319',
    })
    format_dec   = wb.add_format({
        'num_format': '#,##0.00;[Red]-#,##0.00;;@',
        'font_name':  'Courier New',
        'font_size':  9,
    })
    format_yen   = wb.add_format({
        'font_name':  'Arial Narrow',
        'num_format': u'#,##0 円;[Red]-#,##0 円;;@',
        'font_size':  9,
        'font_color': '#003366',
    })
    format_usd   = wb.add_format({
        'font_name':  'Arial Narrow',
        'num_format': u'$ #,##0.00;[Red]$ -#,##0.00;;@',
        'font_size':  9,
        'font_color': '#003366',
    })
    format_date_jpn = wb.add_format({
        'num_format': u'[$-409]YYYY年MM月DD日',
        'font_name':  'Arial',
        'font_size':  9,
        'font_color': '#404040',
    })
    format_time = wb.add_format({
        'num_format': u'hh:mm',
        'font_name':  'Arial',
        'font_size':  9,
        'font_color': '#404040',
    })
    format_datetime_jpn = wb.add_format({
        'num_format': u'[$-409]YYYY年MM月DD日 hh:mm',
        'font_name':  'Arial',
        'font_size':  9,
        'font_color': '#404040',
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

    ### Python XlsxWriter
    ### https://xlsxwriter.readthedocs.io/worksheet.html

    # ws.write(row, col, u'Hello from Python!', format_def )
    ws.write_string(row, col, u'Hello from Python!', format_def )

    ws.write_number(row, col, 12345.768, format_dec )

    ws.write_datetime(row, col, 40000, format_date_jpn )

    # set height of row zero (row 1) to 20
    ws.set_row( 0, 20 )

    # Width of columns B:D set to 30.
    ws.set_column(1, 3, 30)

    # Width of column B set to 30.
    ws.set_column(1, 1, 30)

    # hide a column
    ws.set_column(  0,  0, None, None, {'level': 1, 'hidden': True} ) # A

    # freeze panes
    ws.freeze_panes(1, 4) # zero based. (1, 4) is R2C5 or E2

    wb.close()


def test():
    pass


if __name__=='__main__':

    # logger setup
    logfile = str(sys.argv[0])[:-3] + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

    main()
