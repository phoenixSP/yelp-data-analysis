import numpy as np
import pandas as pd
import xml.etree.ElementTree as ET
files = ["../funny_user_ids.xml", "../useful_user_ids.xml", "../cool_user_ids.xml"]
funny_useful_cool_ids = []
for f in files:
    xml = ET.parse(f)
    ids = []
    for elem in xml.iter():
        ids.append(elem.text)
    funny_useful_cool_ids.append(ids)
#dictionary is now filled with files and ID's
user_file = "../user_name_and_id.xml"
user_xml = ET.parse(user_file)
user_dict = {}
count = 0
value = ""
for e in user_xml.iter():
    if count == 0:
        value = e.text
        count += 1
    elif count == 1:
        user_dict[e.text] = value
        count = 0
funny_people = []
for id in funny_useful_cool_ids[0]:
    funny_people.append(user_dict.get(id))
useful_people = []
for id in funny_useful_cool_ids[1]:
    useful_people.append(user_dict.get(id))
cool_people = []
for id in funny_useful_cool_ids[2]:
    cool_people.append(user_dict.get(id))
funny_people = list(filter(None, funny_people))
useful_people = list(filter(None, useful_people))
cool_people = list(filter(None, cool_people))
print ("Funny People:")
print funny_people
print ("Useful People:")
print useful_people
print ("Cool People:")
print cool_people