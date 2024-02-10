"""if we want to merge pdf files , we can do it with python
we can use pypdf2 mdule
with this module you can merge as many files as you want 
"""

import PyPDF2
from PyPDF2 import PdfMerger, PdfReader

# create the list of files to read
list1 = [r'D:\My_learning\Data_Camp\Functions\hundred\one.pdf', r'D:\My_learning\Data_Camp\Functions\hundred\two.pdf']

merge = PyPDF2.PdfMerger(strict=True)

for file in list1:
    merge.append(PdfReader(file, 'rb'))  # Open files in 'rb' mode

# merge the files and name the merged file
merge.write('mergedfile.pdf')
merge.close()

# reading a created file
created_file = PdfReader('mergedfile.pdf')
print(created_file)

# print the number of pages in the merged PDF
num_pages = len(created_file.pages)
print(f'The merged PDF has {num_pages} pages.')