import PyPDF2

def merge_pdfs(pdf_list,output_path):
    pdf_writer = PyPDF2.PdfWriter()
    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_path,'wb') as out:
        pdf_writer.write(out)
    
    print(f'Merged pdf saved as {output_path}')

input_files = []
for i in range(1,6):
    input_files.append(f'lec{i}.pdf')

output_file = 'mergerd.pdf'

merge_pdfs(input_files,output_file)