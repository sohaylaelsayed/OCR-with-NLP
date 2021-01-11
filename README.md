# OCR-with-NLP
TASK INTRODUCTION:
Data: From https://rrc.cvc.uab.es/?ch=13&com=downloads, go to the Google Drive download link (you'll have to register first) and download text.task1&2-test(361p) folder. You'll need to eliminate extra photos by comparing the names in task3-test and text.task1&2-test

REQUIRMENTS:

1. Install tesseract using windows installer available at: https://github.com/UB-Mannheim/tesseract/wiki

2. Note the tesseract path from the installation. Default installation path at the time of this edit was: C:\Users\USER\AppData\Local\Tesseract-OCR. It may change so please check the installation path.

3. pip install pytesseract

4. Set the tesseract path in the script before calling image_to_string:

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\USER\AppData\Local\Tesseract-OCR\tesseract.exe'

5.pip install tesseract

6.pip install tesseract-ocr

7.nltk.download('punkt')

8. nltk.download('averaged_perceptron_tagger')
