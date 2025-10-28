import sqlite3

def init_db() :
    with sqlite3.connect("backup_data.sqlite3") as conn :
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE if not exists backup_data(id TEXT PRIMARY KEY , backup_name TEXT , backup_date TEXT , backup_type TEXT ,
                        password TEXT , status Text) """)
        conn.commit()