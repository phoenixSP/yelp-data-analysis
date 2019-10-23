def takeSecond(elem):
    return elem[1]
file = "../business_checkin_count.txt"
with open(file,"r") as f:
    city_checkin_count = eval(f.read())
    checkin_list = []
    for city in city_checkin_count:
        if city_checkin_count[city] == 0:
            city_checkin_count[city] = 1
        checkin_list.append((city,city_checkin_count[city]))
    checkin_list.sort(key=takeSecond,reverse=True)
    print checkin_list