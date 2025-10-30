import sqlite3

def init_db(db_path) :
    with sqlite3.connect(db_path) as conn :
        cur = conn.cursor()
        cur.execute(""" CREATE TABLE if not exists backup_data(id TEXT PRIMARY KEY , backup_name TEXT , backup_date TEXT ,
                        status Text) """)
        conn.commit()
