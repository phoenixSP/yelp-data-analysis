#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:44:42 2019

@author: pal00007
"""

import xml.etree.ElementTree as ET
import os

data_folder = "../data"
extracted_info = "advanced2.xml"

extracted_business_info = os.path.join(data_folder, extracted_info)

tree = ET.parse(extracted_business_info)