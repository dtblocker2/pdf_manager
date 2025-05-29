import fitz

def optimize_pdf(input_file,output_file):
    pdf_document = fitz.open(input_file)
    pdf_document.save(output_file,garbage=3,deflate=True)
    print(f"PDF has been optimized as {output_file}")

optimize_pdf('dpp1.pdf','compresseddpp.pdf')