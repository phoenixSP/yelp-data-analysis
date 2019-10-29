import xml.etree.ElementTree as ET
import csv
import json
glendale_xml_file = '../lv_data.xml'
glendale_csv_file = '../../../CSCI5751/Glendale_Data/Restaurant_Inspections.csv'
#city/name/state/stars/address <- BaseX
glendale_basex_xml = ET.parse(glendale_xml_file)
fieldnames = ("Serial Number","Permit Number","Restaurant Name","Location Name","Category Name","Address","City","State","Zip","Current Demerits","Current Grade","Date Current","Inspection Date","Inspection Time","Employee ID","Inspection Type","Inspection Demerits","Inspection Grade","Permit Status","Inspection Result","Violations","Record Updated","Location")
glendale_csv_json = {}
with open(glendale_csv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile,fieldnames)
    for row in reader:
        glendale_csv_json[(row["Address"]).lower()] = row
count = 0
value = []
xml_dict = {}
for e in glendale_basex_xml.iter():
    if count == 0:
        #city
        value = [e.text]
        count += 1
    elif count == 5:
        if e.text is not None:
            xml_dict[e.text.encode('utf-8').lower()] = value
        count = 0
    else:
        value += [e.text]
        count += 1
grade_dict = {}
for addr in xml_dict:
    if addr in glendale_csv_json:
        if glendale_csv_json[addr]["Current Grade"] not in grade_dict:
            grade_dict[glendale_csv_json[addr]["Current Grade"]] = [float(xml_dict[addr][4]),1]
        else:
            avg = grade_dict[glendale_csv_json[addr]["Current Grade"]][0] * grade_dict[glendale_csv_json[addr]["Current Grade"]][1]
            grade_dict[glendale_csv_json[addr]["Current Grade"]][1] += 1
            avg = avg + float(xml_dict[addr][4])
            avg = avg / grade_dict[glendale_csv_json[addr]["Current Grade"]][1]
            grade_dict[glendale_csv_json[addr]["Current Grade"]][0] = avg
print grade_dict