import json
import dicttoxml
import sys

def takeSecond(elem):
    return elem[1]

source_dataset_path = "../data/dataset_no_nulls/"
file = "../business_same_name_count.txt"
name_cnt = {}
with open(source_dataset_path  +'business_no_nulls.json', "r") as ins:
    for line in ins:
        try:
            json_obj = json.loads(line)
            if "name" not in json_obj:
                continue

            name = json_obj["name"]
            if name not in name_cnt:
                name_cnt[name] = 0
            name_cnt[name] = name_cnt[name] + 1
        except ValueError:
            print("err")

bus_list = []
for k, v in name_cnt.items():
    bus_list.append((k, v))
bus_list.sort(key=takeSecond, reverse=True)
with open(file, "w") as out:
    for bus in bus_list:
        out.write(bus[0] + "," + str(bus[1]) + "\n")
