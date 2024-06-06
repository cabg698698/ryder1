import os
import psycopg2

DATABASE_URL = "postgres://ryder_user:v0kNI4Pqp6h5Om1UuzuQmwaAHOcqeTsW@dpg-colmh3a1hbls7391npug-a.singapore-postgres.render.com/ryder"

def search_record(record_list):


    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()

    postgres_insert_query = f"""SELECT * FROM box_data WHERE box_name LIKE '%{record_list}%'"""
    cursor.execute(postgres_insert_query)

    result = cursor.fetchall()

    return result

def update_record(record_list):


    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    if record_list[0] == "新增":
        postgres_insert_query = f"""SELECT {record_list[2]} FROM box_data WHERE box_name LIKE '%{record_list[1]}%'"""
        cursor.execute(postgres_insert_query)
        x = cursor.fetchone()[0]
    else:
        x = ""
    postgres_insert_query = f"""UPDATE box_data SET {record_list[2]}='{x + record_list[3]}' WHERE box_name LIKE '%{record_list[1]}%'"""
    cursor.execute(postgres_insert_query)
    conn.commit()
    cursor.close()
    conn.close()


# def update_record(record_list):
#     if record_list[2] == "地址":
#         column_name = "address"
#     elif record_list[2] == "座標":
#         column_name = "lng_lat"
#     elif record_list[2] == "走法":
#         column_name = "entry_method"
#     elif record_list[2] == "電源":
#         column_name = "source_type"
#     elif record_list[2] == "備註":
#         column_name = "remark"
#     DATABASE_URL = os.environ["DATABASE_URL"]

#     conn = psycopg2.connect(DATABASE_URL, sslmode="require")
#     cursor = conn.cursor()

#     postgres_insert_query = f"""UPDATE box_data SET {column_name}= WHERE '%{record_list}%'"""

#     cursor.execute(postgres_insert_query)
#     result = cursor.fetchall()

#     return result



def insert_record(record_list):


    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    table_columns = "(box_name, address, lng_lat, entry_method, source_type, remark)"
    postgres_insert_query = f"""INSERT INTO box_data {table_columns} VALUES (%s, %s, %s, %s, %s, %s);"""

    cursor.execute(postgres_insert_query, record_list)
    conn.commit()
    result = f"{cursor.rowcount}筆資料新增成功"
    print(result)
    cursor.close()
    conn.close()
    return result

def delete_record(record_list):


    conn = psycopg2.connect(DATABASE_URL, sslmode="require")
    cursor = conn.cursor()
    
    postgres_insert_query = f"""DELETE FROM box_data WHERE box_name='{record_list}'"""
    print(postgres_insert_query)
    cursor.execute(postgres_insert_query)
    conn.commit()
    result = f"{cursor.rowcount}筆資料刪除成功"
    print(result)
    cursor.close()
    conn.close()
    return result
