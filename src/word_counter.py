import json
import dicttoxml
import sys

def takeSecond(elem):
    return elem[1]

source_dataset_path = "../data/dataset_no_nulls/"
file = "../word_count.txt"
word_cnt = {}
with open(source_dataset_path  +'review_no_nulls.json', "r") as ins:
    for line in ins:
        try:
            json_obj = json.loads(line)
            if "text" not in json_obj:
                continue

            text = json_obj["text"].upper()
            words = text.split()
            for w in words:
                if w not in word_cnt:
                    word_cnt[w] = 0
                word_cnt[w] = word_cnt[w] + 1
        except ValueError:
            print("err")

word_list = []
for k, v in word_cnt.items():
    word_list.append((k, v))
word_list.sort(key=takeSecond, reverse=True)
with open(file, "w") as out:
    for word in word_list:
        out.write(word[0] + "," + str(word[1]) + "\n")
