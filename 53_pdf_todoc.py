from pdf2docx import Converter

#path to the pdf fle
pdf_file= 'mergedfile.pdf'

#path to where the doc file will be saved
word_file = 'merfed_doc_file.docx'

#initiate convertor
cv = Converter(pdf_file)

cv.convert(word_file)

#close file

cv.close()

"""Python has a library called pdf2docs. With this library, you can 
convert a pdf file to a word document with just a few lines of 
code. Using pip, install the library;
pip install pdf2docx 
We are going to import the Converter class from this module. 
If the file is in the same directory as your Python script, then 
you can just provide the name of the file instead of a link. The 
new doc file will be saved in the same directory"""