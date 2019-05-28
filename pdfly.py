#!/usr/bin/env python

import argparse
from pdfly import pdf_utils, arg_validation

parser = argparse.ArgumentParser(
    description="Performs basic operations on " "PDF files"
)

subparsers = parser.add_subparsers()
extract_subparser = subparsers.add_parser(
    "extract",
    help="Extract pages from a PDF file",
    description="Extract pages from a PDF file and save them to a new file",
)
extract_subparser.add_argument(
    "infile", type=str, help="Input PDF to be processed"
)
extract_subparser.add_argument(
    "outfile", type=str, help="Path of the output file"
)
extract_subparser.add_argument(
    "from_page",
    type=int,
    help="""First page to be extracted. Both 0 and 1 mean the first page""",
)
extract_subparser.add_argument(
    "to_page",
    type=int,
    help="""Last page to be extracted. 0 means the last one""",
)
extract_subparser.set_defaults(func="extract")

merge_subparser = subparsers.add_parser(
    "merge", help="Tools for merging PDFs or part of them"
)
merge_subparser.add_argument(
    "-o", "--outfile", type=str, help="Path of the output PDF"
)
merge_subparser.add_argument(
    "pdfs_to_merge",
    type=str,
    nargs="+",
    help="""Paths to the PDF files to be merged""",
)
merge_subparser.set_defaults(func="merge")

parser.add_argument(
    "-v", "--verbose", help="Increase output verbosity", action="store_true"
)

args = parser.parse_args()

if args.func == "extract":
    from_page = args.from_page
    to_page = args.to_page
    arg_validation.validate_page_numbers(from_page, to_page)
    pdf_utils.extract(args.infile, args.outfile, from_page, to_page)

elif args.func == "merge":
    pdf_utils.merge(args.outfile, args.pdfs_to_merge)

print(f"Created {args.outfile}")
