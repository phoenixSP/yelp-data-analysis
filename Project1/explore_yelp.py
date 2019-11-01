# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 10:19:01 2019

@author: shrey
"""

import pandas as pd
import numpy as np
import os
import os.path
import time

#%%
data_folder = "/home/pal00007/Documents/big_data/data"

#%%
#exploring business.json
#columns which have null values and their count   
business_df = pd.read_json (os.path.join(data_folder, "business.json"), lines = True)
column_null_count = business_df.isnull().sum()

indexes = np.where(business_df.applymap(lambda x: x == ""))
indexes_np = np.column_stack((indexes[0], indexes[1]))

#number of address that have empty strings
count_empty_address = len(indexes_np[ (indexes_np[:,1] == 2)])


#number of city that have empty strings
count_empty_city= len(indexes_np[ (indexes_np[:,1] == 3)])

#number of postal code that have empty strings
count_empty_postalcode= len(indexes_np[ (indexes_np[:,1] == 5)])

##shorter code
#np.unique(indexes_np[:,1], return_counts= True)

#city count 
#city_count = business_df['city'].value_counts()

#%%
	
checkin_df = pd.read_json (os.path.join(data_folder, "checkin.json"), lines = True)

#columns which have null values and their count            
checkin_column_null_count = checkin_df.isnull().sum()

#%%

review_df = pd.read_json (os.path.join(data_folder, "review.json"), lines = True)

#columns which have null values and their count            
review_column_null_count = review_df.isnull().sum()

#%%
photo_df = pd.read_json (os.path.join(data_folder, "photo.json"), lines = True)

#columns which have null values and their count            
photo_column_null_count = photo_df.isnull().sum()

#%%
tip_df = pd.read_json (os.path.join(data_folder, "tip.json"), lines = True)

#columns which have null values and their count            
tip_column_null_count = tip_df.isnull().sum()

#%%
user_df = pd.read_json (os.path.join(data_folder, "user.json"), lines = True)

#columns which have null values and their count            
user_column_null_count = user_df.isnull().sum()


#%%
#checking if photos have their time of creation
photos_df = pd.read_json("/home/pal00007/Documents/big_data/data/photo.json", lines = True)

print("Last modified: %s" % time.ctime(os.path.getmtime("/home/pal00007/Downloads/photos/Zz_Z_zdp-DmHl32kya81wQ.jpg")))
print("Created: %s" % time.ctime(os.path.getctime("/home/pal00007/Downloads/photos/Zz_Z_zdp-DmHl32kya81wQ.jpg")))

print("Last modified: %s" % time.ctime(os.path.getmtime("/home/pal00007/Downloads/photos/Kly6oql6von9B2ZtdJZ-lA.jpg")))
print("Created: %s" % time.ctime(os.path.getctime("/home/pal00007/Downloads/photos/Kly6oql6von9B2ZtdJZ-lA.jpg")))

