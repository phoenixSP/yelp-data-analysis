# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:19:01 2019

@author: shrey
"""

import pandas as pd
import json
import numpy as np

#%%
#with open(r"C:/Users/shrey/Pictures/yelp_data_folder/business.json", "r", encoding='utf8', errors='ignore') as read_file:
#    data = []
#    for line in read_file:
#        line_contents = json.loads(line)
#        data.append(line_contents)
#        
    
#%%
    

'''
isnull = df.isnull()
isnull_pos = []
for i in range(isnull.shape[0]):
    for j in range(isnull.shape[1]):
        if isnull.iloc[i,j] == True:
            isnull_pos.append([i,j])

np_isnull_pos = np.array(isnull_pos)


null_columns = np.unique(np_isnull_pos[:,1])

#gives the names of the columns that have null values
null_columns_names = [df.columns[i] for i in null_columns]
'''

#%%
#columns which have null values and their count   
business_df = pd.read_json (r"C:/Users/shrey/Pictures/yelp_data_folder/business.json", lines = True)
column_null_count = business_df.isnull().sum()

#city count 
#city_count = business_df['city'].value_counts()

#%%
	
checkin_df = pd.read_json (r"C:/Users/shrey/Pictures/yelp_data_folder/checkin.json", lines = True)

#columns which have null values and their count            
checkin_column_null_count = checkin_df.isnull().sum()

#%%

review_df = pd.read_json (r"C:/Users/shrey/Pictures/yelp_data_folder/review.json", lines = True)

#columns which have null values and their count            
review_column_null_count = review_df.isnull().sum()

#%%
photo_df = pd.read_json (r"C:/Users/shrey/Pictures/yelp_data_folder/photo.json", lines = True)

#columns which have null values and their count            
photo_column_null_count = photo_df.isnull().sum()

#%%
tip_df = pd.read_json (r"C:/Users/shrey/Pictures/yelp_data_folder/tip.json", lines = True)

#columns which have null values and their count            
tip_column_null_count = tip_df.isnull().sum()

#%%
user_df = pd.read_json (r"C:/Users/shrey/Pictures/yelp_data_folder/user.json", lines = True)

#columns which have null values and their count            
user_column_null_count = user_df.isnull().sum()


#%%

photos_df = pd.read_json("/home/pal00007/Documents/big_data/data/photo.json", lines = True)

#%%
import os.path
import time
print("Last modified: %s" % time.ctime(os.path.getmtime("/home/pal00007/Downloads/photos/Zz_Z_zdp-DmHl32kya81wQ.jpg")))
print("Created: %s" % time.ctime(os.path.getctime("/home/pal00007/Downloads/photos/Zz_Z_zdp-DmHl32kya81wQ.jpg")))

#%%

print("Last modified: %s" % time.ctime(os.path.getmtime("/home/pal00007/Downloads/photos/Kly6oql6von9B2ZtdJZ-lA.jpg")))
print("Created: %s" % time.ctime(os.path.getctime("/home/pal00007/Downloads/photos/Kly6oql6von9B2ZtdJZ-lA.jpg")))

