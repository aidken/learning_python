#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import io
import logging
import xlsxwriter

# cSpell:ignore xlsx xlsxwriter datefmt levelname arial


'''
Python template for creating an Excel file.
https://xlsxwriter.readthedocs.io/
'''


def main():

    wb_name = 'tmp.xlsx'
    ws_name = 'Sheet1'

    wb = xlsxwriter.Workbook(wb_name)
    ws = wb.add_worksheet(ws_name)

    # define excel cell formats
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

    # Python XlsxWriter
    # https://xlsxwriter.readthedocs.io/worksheet.html

    # ws.write(row, col, u'Hello from Python!', format_def )
    ws.write_string(row, col, u'Hello from Python!', format_def)

    ws.write_number(row, col, 12345.768, format_dec)

    ws.write_datetime(row, col, 40000, format_dec)

    # set height of row zero (row 1) to 20
    ws.set_row(0, 20)

    # Width of columns B:D set to 30.
    ws.set_column(1, 3, 30)

    # Width of column B set to 30.
    ws.set_column(1, 1, 30)

    # hide a column
    ws.set_column(0, 0, None, None, {'level': 1, 'hidden': True})  # A

    # freeze panes
    ws.freeze_panes(1, 4)  # zero based. (1, 4) is R2C5 or E2

    wb.close()


if __name__ == "__main__":

    # https://qiita.com/jack-low/items/91bf9b5342965352cbeb
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

    # logger setup
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    file_name = str(sys.argv[0])[:-3] + ".log"
    handler_file = logging.FileHandler(file_name)
    handler_file.setLevel(logging.DEBUG)
    formatter_file = logging.Formatter(
        "%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s"
    )
    handler_file.setFormatter(formatter_file)
    logger.addHandler(handler_file)

    # console logger to show INFO messages
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.INFO)
    formatter_console = logging.Formatter("%(name)s: %(levelname)s %(message)s")
    handler_console.setFormatter(formatter_console)
    logger.addHandler(handler_console)

    main()
