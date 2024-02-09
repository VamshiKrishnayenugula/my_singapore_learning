from barcode import ISBN13
from barcode.writer import ImageWriter

from PIL import Image

num = "97856587569924"
#saving image as png

bar_code = ISBN13(num,writer= ImageWriter())

#save image

bar_code.save('bar_code')

#read the image using pillow

img = Image.open("bar_code.png")
img.show()

