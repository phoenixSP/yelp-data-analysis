import json
import dicttoxml
import sys
## This converts json object into xml object
## how to use: python json_to_xml [filename]
## filename could contain .json extension

source_dataset_path = "../data/dataset_no_nulls/"
target_dataset_path = "../data/dataset_xml/"

files = ['business', 'tip' , 'review','checkin','tip','user','photo']
for f in files:
	print("-----Running "+f+" -----")
	error_counter = 0;
	outfile = open(target_dataset_path + f+'.xml', 'wb')
	outfile.write(str.encode('<?xml version="1.0" encoding="UTF-8" ?>'))
	outfile.write(str.encode('<root>'))
	with open(source_dataset_path + f +'_no_nulls.json', "r") as ins:
		for line in ins:
			try:
				json_obj = json.loads(line)
				xml = dicttoxml.dicttoxml(json_obj, root=False)
				outfile.write(str.encode("<"+f+">\n"))
				outfile.write(xml)
				outfile.write(str.encode("</"+f+">\n"))
			except ValueError:
				error_counter +=1
	outfile.write(str.encode('</root>'))
	print(f+" number of erros occured: " + str(error_counter))
	print("-----Done "+f+" -----")
	# subprocess.call(['mv',target_dataset_path + f+'_not_nulls.json','cleandata'])
