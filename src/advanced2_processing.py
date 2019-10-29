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

all_categories = set()

for child in tree.iter('categories'):
    cat = child.text.split(",")
    #print(cat)
    for e in cat: 
        all_categories.add(e.strip())
            
#%%
        
all_categories_list = []

for child in tree.iter('categories'):
    cat = child.text.split(",")
    
    def strip(s):
        return s.strip()
    
    cat = list(map(strip, cat))
    all_categories_list.append(cat)
    
    
    
#%%
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules


te = TransactionEncoder()
te_ary = te.fit(all_categories_list).transform(all_categories_list)
df = pd.DataFrame(te_ary, columns=te.columns_)
frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)   

#%%

res = association_rules(frequent_itemsets, metric="confidence", min_threshold=1)

#%%
