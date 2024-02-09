"""You can convert text into handwriting with Python. Python has 
a module called pywhatkit. Install pywhatkit using pip.
pip install pywhatkit
Below, we use pywhatkit to convert text to handwriting and 
save it as an image. We then use the cv2 library to view the 
image. Run this code below:"""

import pywhatkit
import cv2 as cv
# text to convert to handwriting
text = 'Python is great' 
# converting text to handwriting and saving as image
pywhatkit.text_to_handwriting(text, 
save_to='new_text.png')
# reaading image using cv
hand_text = cv.imread("new_text.png")
cv.imshow("hand_text", hand_text)
cv.waitKey(0)
cv.destroyAllWindows()
