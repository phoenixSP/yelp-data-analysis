import xml.etree.ElementTree as ET
business_file = "../business_biz_id.xml"
business_xml = ET.parse(business_file)
business_dict = {}
count = 0
value = ""
city = ""
for e in business_xml.iter():
    if count == 0:
        #business_id
        value = e.text
        count += 1
    elif count == 1:
        #city
        if e.text in business_dict:
            business_dict[e.text] = business_dict[e.text] + [value]
        else:
            business_dict[e.text] = [value]
        count = 0
#dictionary is filled with city:[business_ids]
checkin_file = "../checkin_biz_id.xml"
checkin_xml = ET.parse(checkin_file)
#iterate through checkin ids and count how many checkins for each city
city_count = {}
for id in checkin_xml.iter():
    for d in business_dict:
        if id.text in business_dict[d]:
            if d in city_count:
                city_count[d] = city_count.get(d) + 1
            else:
                city_count[d] = 0
print city_count
