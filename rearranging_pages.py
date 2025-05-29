import PyPDF2

def rearraging_pages(pdf_path, output_pdf,page_order):
    pdf_reader = PyPDF2.PdfReader(pdf_path)
    pdf_writer = PyPDF2.PdfWriter()
    
    for page_num in page_order:
        pdf_writer.add_page(pdf_reader.pages[page_num-1])
        

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)  
    print(f'Saved: {output_pdf}')

# Example usage:
rearraging_pages('dpp1.pdf', 'rearrangedapp1.pdf',[3,1,2])
