import pdfplumber

def extract_text(pdf_path,output_file):
    with pdfplumber.open(pdf_path) as pdf:
        i = 1
        for page in pdf.pages:
            page_text = f'Page No: {i}'
            i += 1
            page_text += '\n'+page.extract_text()+'\n'

            with open(output_file,'a') as output:
                try:
                    output.write(page_text)
                except UnicodeEncodeError as e:
                    print(e)

        print(f"Extracted text has been save as {output_file}")

extract_text('dpp1.pdf','extracted text.txt')