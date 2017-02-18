#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pytest
import os
import jinja2


# find absolute path of the running file
# https://pythonadventures.wordpress.com/2014/02/25/jinja2-example-for-generating-a-local-file-using-a-template/
PATH = os.path.dirname( os.path.abspath( __file__ ) )

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader( os.path.join( PATH, 'templates' ) )
)

def render_template(template_filename, stash):
    return env.get_template(template_filename).render(stash)


def main():

    output_filename   = 'output.html'
    template_filename = 'test.html'

    title  = u'Hello Jijna2!'
    sample = u'これは日本語です。'

    stash = {
        'title':  title,
        'sample': sample,
    }

    with open(output_filename, 'w') as f:
        html = render_template(template_filename, stash)
        f.write(html)


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
