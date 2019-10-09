import json
import dicttoxml
import sys
## This converts json object into xml object
## how to use: python json_to_xml [filename]
## filename could contain .json extension

source_dataset_path = "../data/dataset_no_nulls/"
target_dataset_path = "../data/dataset_xml/"

if len(sys.argv) < 0:
	print("specify source file name!")
	exit()

source = sys.argv[1]
if source[-5:] == '.json':
	source = source[:-5]

source_file = source_dataset_path + source + ".json"
target_file = target_dataset_path + source + ".xml"

with open(source_file, 'r') as f:
	json_dict = json.load(f) #json -> dict
	xml = dicttoxml.dicttoxml(json_dict)

with open(target_file,'wb') as f:
	f.write(xml)