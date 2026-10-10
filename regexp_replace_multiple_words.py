#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import logging
import argparse
import re

# cSpell:ignore datefmt levelname infile

# get logger of this library __name__ and attach a null handler
logger = logging.getLogger(__name__)

_REPLACEMENT_DICT = {
    'apple' : 'orange',
    'banana': 'grape'
}

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('input_path', type='str', help='path to the input file.')
    arg_parser.add_argument('output_path', type='str', help='path to the output file.')

    group = arg_parser.add_mutually_exclusive_group()
    group.add_argument("-r", "--replace_multiple_words_case_insensitive", action="store_true", help="call replace_multiple_words_case_insensitive.")
    group.add_argument("-b", "--bbb", action="store_true", help="Do BBB.")
    group.add_argument("-c", "--ccc", action="store_true", help="Do CCC.")
    group.add_argument("-d", "--ddd", action="store_true", help="Do DDD.")

    args = arg_parser.parse_args()

    # if no argument is passed, show help
    if len(sys.argv) == 1:
        arg_parser.print_help(sys.stderr)
        sys.exit(1)

    elif args.replace_multiple_words_case_insensitive():
        replace_multiple_words_case_insensitive(
            input_path       = args.input_path,
            output_path      = args.output_path,
            replacement_dict = _REPLACEMENT_DICT,
        )
    elif args.bbb:
        bbb()
    elif args.ccc:
        ccc()
    elif args.ddd:
        ddd()
    else:
        arg_parser.print_help()


def replace_multiple_words_case_insensitive(input_path, output_path, replacement_dict=_REPLACEMENT_DICT):
    # 1. Force all dictionary keys to lowercase for safe lookup later
    lower_dict = {key.lower(): val for key, val in replacement_dict.items()}

    # 2. Sort by length descending (using the original keys is fine for length)
    sorted_words = sorted(replacement_dict.keys(), key=len, reverse=True)

    # 3. Create the pattern
    pattern_string = r'\b(' + '|'.join(re.escape(word) for word in sorted_words) + r')\b'

    # 4. Add flags/options here if you want
    compiled_pattern = re.compile(pattern_string, flags=re.IGNORECASE)

    # 5. The callback function
    def replace_match(match):
        # match.group(0) is guaranteed to exist here!
        word_found = match.group(0).lower()  # Convert found word to lowercase to match our dictionary
        return lower_dict[word_found]

    # 6. Stream and process
    with (
        open(input_path, 'r', encoding='utf-8') as infile,
        open(output_path, 'w', encoding='utf-8') as outfile
    ):
        # with one with statement, you can open multiple file handles
        # from 3.10. no longer need nested with's.
        for line in infile:
            # sub() searches from the beginning of line. it invokes callback
            # multiple times if it finds more than one matches.
            modified_line = compiled_pattern.sub(replace_match, line)
            outfile.write(modified_line)


def bbb():
    logger.info("This is INFO, inside function aaa().")
    logger.debug("This is DEBUG, inside function aaa().")
    logger.warning("This is WARNING, inside function aaa().")
    logger.error("This is ERROR, inside function aaa().")
    pass


def ccc():
    pass


def ddd():
    pass


if __name__ == "__main__":
    main()
