# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 21:43:16 2021

@author: sohay
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
from pytesseract import Output
import re 
import json 
from os import listdir
from os.path import isfile, join
import nltk
from nltk.tokenize import word_tokenize
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
import os 

def ImagePrpcessing():
    restaurantNameForImage=[]
    
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 
    imageFile = [f for f in listdir('D:\computer vision\task3-test 347p) --20210105T182511Z-001\task3-test 347p) -\task3-test（347p)') if isfile(join('D:\computer vision\task3-test 347p) --20210105T182511Z-001\task3-test 347p) -\task3-test（347p)', f))]
    
    for image in imageFile:
        receipt_ocr = {}
        img = cv2.imread(image)
    
    # Simple thresholding
    
        ret,thresh1 = cv2.threshold(img,210,255,cv2.THRESH_BINARY)
        #cv2.imshow(thresh1,'gray')
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        n_boxes = len(d['level'])
        for i in range(n_boxes):
        	(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])    
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        img = cv2.imread(image)
        cv2.imshow(img,'img')
        extracted_text = pytesseract.image_to_string(img, lang = 'eng')
        splits = extracted_text.splitlines()
        restaurant_name = splits[0] + '' + splits[1]
        restaurantNameForImage.append(restaurant_name)
        
        # regex for date. The pattern in the receipt is in 30.07.2007 in DD:MM:YYYY
        
        date_pattern = r'(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d'
        date = re.search(date_pattern, extracted_text).group()
        receipt_ocr['date'] = date
        print(date)
        
        for line in splits:
          print(line)
          if re.search(r'Total', line):
            total = line
        
        
        total = total.split[-1]
        
        # Store the results in the dict
        
        receipt_ocr['total'] = total
        receipt_ocr['restaurant_name']=restaurant_name
        
        
        receipt_json = json.dumps(receipt_ocr)
        print(receipt_json)
    return restaurantNameForImage

def textProcessing():
    arrayofnameRestaurant=ImagePrpcessing() 
    nlp = en_core_web_sm.load() 
    recipetFile = [f for f in listdir('D:\computer vision\text.task1&2-test（361p)-20210105T182136Z-001\text.task1_2-test（361p)') if isfile(join('D:\computer vision\text.task1&2-test（361p)-20210105T182136Z-001\text.task1_2-test（361p)', f))]
    for recipet in recipetFile:
        with open(recipet) as myfile:
            restaurantNameForText=[] # to save the restaurant name 
            samples = [] #array to store all data from each file 
            for line in myfile.readlines():
                result = re.sub(r'[0-9,*]+', '', line)             
                samples.append(result)
            for token in samples:
             sent = nltk.sent_tokenize(token)
             doc=nlp(token)
             NER=([(X.text, X.label_) for X in doc.ents])
             if NER[1]=='ORG':
               restaurantNameForText.append(sent)
               
        for name in range(len(restaurantNameForText)):
         if restaurantNameForText not in arrayofnameRestaurant:
          os.remove(recipet)


    