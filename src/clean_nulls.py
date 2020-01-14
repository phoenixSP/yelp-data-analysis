import json
import numpy as np
import pandas as pd
import subprocess
import os
import time 
import getpass

st = time.time()

data_folder = "/home/pal00007/Documents/big_data/CSCI5751/data"
source_dataset_path = "/home/pal00007/Documents/big_data/data/"
target_dataset_path = "/home/pal00007/Documents/big_data/data_null/"

#subprocess.call(['mkdir','cleandata'])
#files = ['business', 'tip' , 'review','checkin','tip','user','photo']

files = ['checkin']

for f in files:
    print("-----Running "+f+" -----")
    print(f+".json size with NULLs: "+str(os.path.getsize(source_dataset_path + f +'.json')))
    review_df = pd.DataFrame([])
    reader = pd.read_json(source_dataset_path + f +'.json', lines=True, chunksize=250000)
    for chunk in reader:
        review_df = review_df.append(chunk)
        null_free_df = review_df.dropna()
        joined_df = null_free_df.to_json(orient='records', lines=True)
        outfile = open(target_dataset_path + f+'_no_nulls.json', 'a')
        outfile.write(joined_df)
        review_df = pd.DataFrame([])
        
    print(f+"_not_nulls.json size without NULLs: "+str(os.path.getsize(target_dataset_path + f+'_no_nulls.json')))
    # subprocess.call(['mv',target_dataset_path + f+'_not_nulls.json','cleandata'])#code related to provenance

et = time.time()
username = getpass.getuser()
print(username, "clean_nulls.py", "cleaning nulls from all jsons, creating filename_no_nulls.json", st, et, file= open(os.path.join(data_folder,'provenance.txt'), 'a'))