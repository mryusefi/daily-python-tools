import PyPDF2 
import sys
def load_pdf(file_path):
    try:
        reader = PyPDF2.PdfReader(file_path)
        return reader
    except Exception as e:
        print(f"Error loading PDF file {file_path}: {e}")
        return None 

def merge_pdfs(pdf_list, output_path):
    writer = PyPDF2.PdfWriter()
    for pdf in pdf_list:
        if pdf:
            writer.append(pdf)

    try:
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)
        print(f"PDFs merged successfully into {output_path}")
    except Exception as e:
        print(f"Error writing merged PDF to {output_path}: {e}")


pdf_files = []
for pdf_name in sys.argv[1:]:
    if not pdf_name.endswith('.pdf'):
        print(f"Skipping {pdf_name}, not a PDF file.")
        continue
    pdf_files.append(load_pdf(pdf_name))
    print(f"Loaded {pdf_name}")

merge_pdfs(pdf_files, 'merged_output.pdf')