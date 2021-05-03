from getpass import getpass

from pikepdf import Pdf
from pikepdf._qpdf import PasswordError
from PyPDF2 import PdfFileReader, PdfFileWriter


def _open_pdf(pdf_path):
    """Simple wrapper arout `pikepdf.Pdf.open`.

    This will prompt for a password when the pdf is encrypted, with an unlimited
    amount of retries
    """
    is_open = False
    password = ""
    while not is_open:
        try:
            input_ = Pdf.open(pdf_path, password=password)
            is_open = True
        except PasswordError:
            password = getpass()
    return input_


def extract(document, new_document, from_page=0, to_page=0):
    """
    Split the PDF document beginning in from_page to to_page included.

    A value of 0 for from_page will mean beginning of the document, and a value
    of 0 for to_page will mean the end of the document
    """

    input_ = _open_pdf(document)
    pages = input_.pages
    num_pages = len(pages)

    from_page = 1 if from_page == 0 else from_page
    to_page = num_pages if to_page == 0 else to_page

    extracted_pages = pages[from_page - 1 : to_page]

    output = Pdf.new()
    output.pages.extend(extracted_pages)
    output.save(new_document)
    return 0


def _add_full_pdf_to_writer(pdf_writer, pdf_reader):
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        pdf_writer.addPage(page)
    return pdf_writer


def merge(new_document, file_list):
    pdf_writer = PdfFileWriter()
    for filepath in file_list:
        pdf_file = PdfFileReader(open(filepath, "rb"))
        pdf_writer = _add_full_pdf_to_writer(pdf_writer, pdf_file)
    with open(new_document, "wb") as outfile:
        pdf_writer.write(outfile)
