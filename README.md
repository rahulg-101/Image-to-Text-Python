# Image-to-Text-Python
This project aims to convert an image containing textual information into its equivalent textual form using Python programming language. The project uses Optical Character Recognition (OCR) technology to recognize and extract the text from the input image.

### Requisites for project
1. Install tesseract using windows installer available at: @https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

3. Use the command to install pytesseract which is a tesseract module built for python using :  pip install pytesseract

4. Set the tesseract path in the script before calling image_to_string:  
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

### License

This project is licensed under the MIT License - see the @https://chat.openai.com/LICENSE file for details.
