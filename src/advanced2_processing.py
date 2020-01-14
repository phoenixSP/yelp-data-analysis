#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 18:44:42 2019

@author: pal00007
"""

import xml.etree.ElementTree as ET
import os
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules
import time 
import getpass
from collections import defaultdict
import json 

st = time.time()

data_folder = "/home/pal00007/Documents/big_data/CSCI5751/data"
extracted_info = "advanced2.xml"

extracted_business_info = os.path.join(data_folder, extracted_info)

tree = ET.parse(extracted_business_info)
        
all_categories_list = []

for child in tree.iter('categories'):
    cat = child.text.split(",")
    
    def strip(s):
        return s.strip()
    
    cat = list(map(strip, cat))
    all_categories_list.append(cat)

te = TransactionEncoder()
te_ary = te.fit(all_categories_list).transform(all_categories_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)   
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))

#subset_1 = frequent_itemsets[ (frequent_itemsets['length'] == 1) & (frequent_itemsets['support'] >= 0.01)]

res = association_rules(frequent_itemsets, metric="confidence", min_threshold=1)
res['consequent_len'] = res['consequents'].apply(lambda x: len(x))

#extracting the data where length of the consequent is 1
res_1 = res[ (res['consequent support'] >= 0.05) & (res['consequent_len'] == 1) ]

#extracting
main_categories = res_1['consequents'].tolist()

#business_latlong
new_list = []
for e in main_categories:
    (x), = e
    new_list.append(x)
    
new_list = set(new_list)


business_latlong = defaultdict(list)

root = tree.getroot()
for child in root: 
    categories = set(child.find('categories').text.split(',')) 
    high_level_category = categories.intersection(new_list)
    
    if len(high_level_category) > 0:
        (high_level_category), = high_level_category
        lat = child.find('latitude').text
        long = child.find('longitude').text
        loc = [lat, long]
        
        business_latlong[high_level_category].append(loc)


file = json.dumps(business_latlong)
f = open(os.path.join(data_folder, "business_latlong_json1.json"), "w")
f.write(file)
f.close()

f = open(os.path.join(data_folder, "business_latlong_txt1.txt"), "w")
f.write(str(business_latlong))
f.close()


#code related to provenance
et = time.time()
username = getpass.getuser()
print(username, "advanced2_processing.py", "creating business_latlong_json.json and business_latlong_text.json", st, et, file= open(os.path.join(data_folder,'provenance.txt'), 'a'))