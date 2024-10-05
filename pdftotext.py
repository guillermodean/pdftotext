import os
import PyPDF2

# Function to extract text from a single PDF file
def extract_text_from_pdf(pdf_path):
    pdf_file_obj = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[page_num]  # Corrected line
        text += page_obj.extract_text()
    pdf_file_obj.close()
    return text

# Function to save extracted text to a TXT file
def save_text_to_txt(text, txt_path):
    # Open the text file with utf-8 encoding
    with open(txt_path, 'w', encoding='utf-8') as txt_file_obj:
        txt_file_obj.write(text)
    txt_file_obj.close()

# Function to find all PDF files in a given directory
def find_all_pdfs(pdf_path):
    files = os.listdir(path=pdf_path)
    return [file for file in files if file.endswith('.pdf')]

# Main script
# Use environment variable for the username in the path
user_name = os.environ.get('USERNAME')
pdf_folder = f'C:/Users/{user_name}/Desktop/python/pdftotext/pdf'

# Find all PDF files in the specified folder
pdf_files = find_all_pdfs(pdf_folder)

# Process each PDF file
for pdf_file in pdf_files:
    pdf_path = os.path.join(pdf_folder, pdf_file)
    txt_path = pdf_file.replace('.pdf', '.txt')
    
    # Extract text from PDF
    print(f'Converting {pdf_file} to text...')
    text = extract_text_from_pdf(pdf_path)
    
    # Save text to TXT file
    save_text_to_txt(text, txt_path)
    
    # Remove the original PDF file
    os.remove(pdf_path)
    print(f'{pdf_file} has been converted and removed.')

print('All PDF files have been converted and removed.')