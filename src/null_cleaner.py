import json
import numpy as np
import pandas as pd
import sys

## This drops rows that contains null 
## how to use: python null_cleaner [filename]
## filename could contain .json extension

source_dataset_path = "../data/dataset_original/"
target_dataset_path = "../data/dataset_no_nulls/"

if len(sys.argv) < 0:
	print("specify source file name!")
	exit()

source = sys.argv[1]
if source[-5:] == '.json':
	source = source[:-5]
	
source_file = source_dataset_path + source + ".json"
target_file = target_dataset_path + source + "_no_nulls.json"

df = pd.read_json (source_file, lines = True)
null_free_df = df.dropna()
null_free_json = null_free_df.to_json(orient='records')
outfile = open(target_file, "w")
outfile.write(null_free_json)