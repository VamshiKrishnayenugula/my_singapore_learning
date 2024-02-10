import cv2 as cv
img = cv.imread(r'D:\My_learning\Data_Camp\Functions\hundred\vamshi_photo.JPG')
# show the original image
img1 = cv.imshow('Original', img)
cv.waitKey(5)
# Converting image to Gray
grayed_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# Show grayed-out image
img2 = cv.imshow('grayed_image', grayed_img)
cv.waitKey(5000)
#Save image
cv.imwrite('grayed.jpg', grayed_img)


"""Do you want to convert a color image into grayscale? Use 
Python’s cv2 module.
First install cv2 using > pip install opencv-python<
Below we are converting a color book image to grayscale. You 
can replace that with your own image. You must know where 
the image is stored.
When you want to view an image using CV2, a window will 
open. The waitkey indicates how long we expect the display 
window to be open. If a key is pressed before the display time is 
over, the window will be destroyed or closed"""