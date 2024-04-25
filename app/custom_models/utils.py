import re

def search_record(text):
    text_list = text.split(" ")
    record = text_list[1].upper()
    return record

def update_record(text):
    record_list = re.split(":|：", text)
    record_list[1] = record_list[1].upper()
    if record_list[2] == "備註":
        record_list[2] = "remark"
    elif record_list[2] == "走法":
        record_list[2] = "entry_method"
    elif record_list[2] == "電源":
        record_list[2] = "source_type"
    elif record_list[2] == "地址":
        record_list[2] = "address"
    elif record_list[2] == "座標":
        record_list[2] = "lng_lat"
    else:
        record_list[2] = "錯誤"
    return record_list


def insert_record(text):
    text_list = text.split("\n")
    record_list = []
    for i in text_list[1:]:
        items = i.split(" ")
        box_name = items[0]
        address = items[1]
        lng_lat = items[2]
        entry_method = items[3]
        source_type = items[4]
        remark = items[5]

        record = (box_name,address,lng_lat,entry_method,source_type,remark)
        record_list.append(record)
    return record_list

def delete_record(text):
    text_list = text.split("\n")
    record = text_list[1]
    return record
