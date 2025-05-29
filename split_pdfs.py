import PyPDF2
import os

def split_pdf(pdf_path, output_dir,page_per_splitted_pdf):
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists

    pdf_reader = PyPDF2.PdfReader(pdf_path)
    
    for page_num in range(len(pdf_reader.pages)//page_per_splitted_pdf):
        pdf_writer = PyPDF2.PdfWriter()
        for i in [page_per_splitted_pdf*page_num+k for k in range(page_per_splitted_pdf)]:
            if i < len(pdf_reader.pages):
                pdf_writer.add_page(pdf_reader.pages[i])
        
        output_path = os.path.join(output_dir, f'page_{page_num + 1}.pdf')

        with open(output_path, 'wb') as out:
            pdf_writer.write(out)
        
        print(f'Saved: {output_path}')

# Example usage:
split_pdf('lec1.pdf', 'splitted_pdfs',3)
