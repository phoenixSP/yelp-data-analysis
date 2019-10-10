import json
import numpy as np
import pandas as pd
import subprocess
import os

source_dataset_path = "../data/dataset_original/"
target_dataset_path = "../data/dataset_no_nulls/"

#subprocess.call(['mkdir','cleandata'])
files = ['business', 'tip' , 'review','checkin','tip','user','photo']
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
    # subprocess.call(['mv',target_dataset_path + f+'_not_nulls.json','cleandata'])