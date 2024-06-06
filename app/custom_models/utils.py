import re

def search_record(text):
    text_list = re.split(":|：", text)
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
    text_list = re.split(":|：", text)
    record_list = [text_list[1].upper(),text_list[2],text_list[3],text_list[4],text_list[5],text_list[6]]
    return record_list

def delete_record(text):
    text_list = re.split(":|：", text)
    record = text_list[1].upper()
    return record
