#! /usr/bin/python
from __future__ import print_function
from PyPDF2 import PdfFileWriter, PdfFileReader

def extract(document, new_document, from_page=0, to_page=0):
    """
    Split the PDF document beginning in from_page to to_page included.

    A value of 0 for from_page will mean beginning of the document, and a value
    of 0 for to_page will mean the end of the document
    """
    page_validation = validate(from_page, to_page)
    if not page_validation['check']:
        raise ValueError(page_validation['message'])
        return 1

    output = PdfFileWriter()
    input1 = PdfFileReader(open(document, "rb"))

    if to_page == 0:
        to_page = input1.getNumPages()
    if from_page == 0:
        from_page = 1

    for i in range(from_page - 1, to_page):
        output.addPage(input1.getPage(i))

    outputStream = file(new_document, "wb")
    output.write(outputStream)
    return 0

def validate(from_page, to_page):
    if not isinstance(from_page, int) or not isinstance(to_page, int):
        return {'check': False, 'message': 'Page numbers must be integers'}
    elif from_page < 0 or to_page < 0:
        return {'check': False, 'message': 'Page numbers must be positive integers'}
    elif (from_page > to_page) and to_page != 0:
        return {'check': False, 'message': 'from_page must be smaller than to_page'}
    else:
        return {'check':True, 'message': ''}

def main():
    output = PdfFileWriter()
    input1 = PdfFileReader(open("document1.pdf", "rb"))

    # print how many pages input1 has:
    print("document1.pdf has %d pages." % input1.getNumPages())

    # add page 1 from input1 to output document, unchanged
    output.addPage(input1.getPage(0))

    # add page 2 from input1, but rotated clockwise 90 degrees
    output.addPage(input1.getPage(1).rotateClockwise(90))

    # add page 3 from input1, rotated the other way:
    output.addPage(input1.getPage(2).rotateCounterClockwise(90))
    # alt: output.addPage(input1.getPage(2).rotateClockwise(270))

    # add page 4 from input1, but first add a watermark from another PDF:
    page4 = input1.getPage(3)
    watermark = PdfFileReader(open("watermark.pdf", "rb"))
    page4.mergePage(watermark.getPage(0))
    output.addPage(page4)


    # add page 5 from input1, but crop it to half size:
    page5 = input1.getPage(4)
    page5.mediaBox.upperRight = (
        page5.mediaBox.getUpperRight_x() / 2,
        page5.mediaBox.getUpperRight_y() / 2
    )
    output.addPage(page5)

    # add some Javascript to launch the print window on opening this PDF.
    # the password dialog may prevent the print dialog from being shown,
    # comment the the encription lines, if that's the case, to try this out
    output.addJS("this.print({bUI:true,bSilent:false,bShrinkToFit:true});")

    # encrypt your new PDF and add a password
    password = "secret"
    output.encrypt(password)

    # finally, write "output" to document-output.pdf
    outputStream = file("PyPDF2-output.pdf", "wb")
    output.write(outputStream)

if __name__ == '__main__':
    # main()
    extract("document1.pdf", "splitted.pdf", to_page=5)
    # print(pages_are_valid(3, 3))
    # print(pages_are_valid(4, 3))
    # print(pages_are_valid(3, 'a'))
