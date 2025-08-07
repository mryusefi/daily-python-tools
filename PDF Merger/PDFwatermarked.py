from PyPDF2 import PdfWriter, PdfReader
from typing import Union, Literal, List
import sys

def load_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        return reader
    except Exception as e:
        print(f"Error loading PDF file {file_path}: {e}")
        return None 

def watermark(
    content_pdf,
    stamp_pdf,
    pdf_result,
    page_indices: Union[Literal["ALL"], List[int]] = "ALL",
):
    reader = content_pdf
    if page_indices == "ALL":
        page_indices = list(range(0, len(reader.pages)))

    writer = PdfWriter()
    for index in page_indices:
        content_page = reader.pages[index]
        mediabox = content_page.mediabox

        # You need to load it again, as the last time it was overwritten
        reader_stamp = PdfReader(stamp_pdf)
        image_page = reader_stamp.pages[0]

        image_page.merge_page(content_page)
        image_page.mediabox = mediabox
        writer.add_page(image_page)

    with open(pdf_result, "wb") as fp:
        writer.write(fp)



#pdf_files = []
watermark_pdf = sys.argv[1]

for pdf_name in sys.argv[2:]:
    if not pdf_name.endswith('.pdf'):
        print(f"Skipping {pdf_name}, not a PDF file.")
        continue
    pdf_file = load_pdf(pdf_name)
    watermark(pdf_file,watermark_pdf, f"watermarked_{pdf_name}.pdf","ALL")
    