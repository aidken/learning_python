#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import pymongo

def main():

    client     = pymongo.MongoClient
    db         = client.test_database
    collection = db.test_collection
    print(collection)


if __name__=='__main__':

    # logger setup
    logfile = str(sys.argv[0]) + '.log'
    logging.basicConfig(
        filename = logfile,
        format   = '%(asctime)s - %(filename)s: %(lineno)s: %(funcName)s - %(levelname)s: %(message)s',
        # level    = logging.DEBUG,
        level    = logging.ERROR,
    )

    main()

