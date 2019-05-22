from PyPDF2 import PdfFileWriter, PdfFileReader


def extract(document, new_document, from_page=0, to_page=0):
    """
    Split the PDF document beginning in from_page to to_page included.

    A value of 0 for from_page will mean beginning of the document, and a value
    of 0 for to_page will mean the end of the document
    """

    output = PdfFileWriter()
    input1 = PdfFileReader(open(document, "rb"))

    if from_page == 0:
        from_page = 1

    if to_page == 0:
        to_page = input1.getNumPages()

    for i in range(from_page - 1, to_page):
        output.addPage(input1.getPage(i))

    outputStream = file(new_document, "wb")
    output.write(outputStream)
    return 0


def _add_full_pdf_to_writer(pdf_writer, pdf_reader):
    for i in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(i)
        pdf_writer.addPage(page)
    return pdf_writer


def merge(outfile, file_list):
    pdf_writer = PdfFileWriter()
    for filepath in file_list:
        pdf_file = PdfFileReader(open(filepath, "rb"))
        pdf_writer = _add_full_pdf_to_writer(pdf_writer, pdf_file)
    output_stream = file(outfile, "wb")
    pdf_writer.write(output_stream)
