# Image-to-Text-Python
This project aims to convert an image containing textual information into its equivalent textual form using Python programming language. The project uses Optical Character Recognition (OCR) technology to recognize and extract the text from the input image. 

### Requisites for project
To run this project, you need to have Python,Opencv and pytesseract installed on your machine.

Steps to install pytesseract : 
1. Install tesseract using windows installer available at: @https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

3. Use the command to install pytesseract which is a tesseract module built for python using :  pip install pytesseract

4. Set the tesseract path in the script before calling image_to_string:  
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'
    
### Usage
OpenCV conveniently handles reading and writing a wide variety of image file formats (e.g., JPG, PNG, TIFF). The library also simplifies displaying an image on screen and allowing user interaction with the opened window.

If an image cannot be read by OpenCV, you should carefully check if the input filename was given correctly, as the cv2.imread function returns a NoneType Python object upon failure. 

Pytesseract, also known as Python-tesseract, is a Python library that enables Optical Character Recognition (OCR). This tool is capable of detecting and extracting text from various sources, such as images, license plates, and more.
    
### Limitations
I have added a few samples of .png and .jpeg files to test which are approximately accurate as the project find it difficult to extract texts from curly fonts although.

### License

This project is licensed under the MIT License - see the @https://chat.openai.com/LICENSE file for details.
