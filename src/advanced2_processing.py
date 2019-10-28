#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:44:42 2019

@author: pal00007
"""

import xml.etree.ElementTree as ET
import os

data_folder = "/home/pal00007/Documents/big_data/CSCI5751/data"
extracted_info = "advanced2.xml"

extracted_business_info = os.path.join(data_folder, extracted_info)

tree = ET.parse(extracted_business_info)

#%%

root = tree.getroot()

for child in tree.iter('categories'):
    print(child.text[0])
    
    #process the string and parse as elements seperated by comma
    #store it in a set/dictinary 