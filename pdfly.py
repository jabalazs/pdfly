#!/usr/bin/python
from __future__ import print_function
import argparse
from pdfly import (pdf_utils, type_validation)
import sys

parser = argparse.ArgumentParser(description='Performs basic operations on PDF files')
parser.add_argument('-v', '--verbose', help='Increase output verbosity',
                    action='store_true')
parser.add_argument('infile', type=str, help='Input PDF to be processed')
parser.add_argument('outfile', type=str, help='Path of the output file')
parser.add_argument('-e',
                    '--extract',
                    type=int,
                    help="""Extracts the selected range of pages from the input
                    PDF and saves it to the specified output. beginning_page equals 0
                    is equivalent to the first page; end_page equals 0 is equivalent
                    to the last page""",
                    nargs=2,
                    metavar=('from_page', 'to_page'))

args =  parser.parse_args()

if args.extract is not None:
    from_page = args.extract[0]
    to_page = args.extract[1]
    type_validation.validate_extract_pages(from_page, to_page)
    pdf_utils.extract(args.infile, args.outfile, from_page, to_page)
    sys.exit(0)
