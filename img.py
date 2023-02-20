import pytesseract
import cv2

#Now we will read the image file from our directory (Note: Image should be in the same folder as your .py file)
img = cv2.imread('2003.jpg')
# Resizing of the image
img = cv2.resize(img, (720, 480))

# Used to set the path for tesseract.exe file which will help in extracting the text from images
pytesseract.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(img)) #Converting image to strings

# To display the image
cv2.imshow('Result', img)
# To make sure that image stays on screen for infinite time
cv2.waitKey(0)

