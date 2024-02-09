import PyPDF2
#open pdf file

file_name = open('mergedfile.pdf','rb')

#read file

read_file = PyPDF2.PdfReader(file_name)

#read fom a specified page

page = read_file._get_page(100)

print(page.extract_text())

file_name.close()