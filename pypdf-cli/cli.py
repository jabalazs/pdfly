#!/usr/bin/python
from __future__ import print_function
import argparse
import pdf_utils
import sys

parser = argparse.ArgumentParser(description='Performs basic operations on PDF files')
parser.add_argument('-v', '--verbose', help='Increase output verbosity',
                    action='store_true')
parser.add_argument('infile', type=str, help='Input PDF to be processed')
parser.add_argument('outfile', type=str, help='Path of the output file')
parser.add_argument('-e',
                    '--extract',
                    type=int,
                    help='Extracts the selected range of pages from the input\
                    PDF and saves it to the specified output. beginning_page equals 0\
                    is equivalent to the first page; end_page equals 0 is equivalent\
                    to the last page',
                    nargs=2,
                    metavar=('beginning_page', 'end_page'))

args =  parser.parse_args()

if args.extract is not None:
    pdf_utils.extract(args.infile, args.outfile, args.extract[0], args.extract[1])
    sys.exit(0)
