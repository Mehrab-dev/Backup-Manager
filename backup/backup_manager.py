import os
import shutil
import datetime
import sqlite3
import uuid
import zipfile

from .config_logger import logger
from .db import init_db

class Backup() :
    def __init__(self,origin_path:str,destination_path:str) :
        self.origin_path = origin_path
        self.destination_path = destination_path
    def backup(self) :
        try :
            if os.path.exists(self.origin_path) :
                if os.path.isdir(self.origin_path) :
                    if not os.path.exists(self.destination_path) :
                        os.makedirs(self.destination_path,exist_ok=True)
                    now_for_db = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    now_for_name = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
                    name = os.path.join(self.destination_path,now_for_name)
                    shutil.make_archive(name,"zip",self.origin_path)
                    logger.info(f"Folder successfully Backed up as {name}.zip")
                    uid = str(uuid.uuid4())
                    db_path = os.path.join(self.destination_path,"backup_data.sqlite3")
                    init_db(db_path)
                    with sqlite3.connect(db_path) as conn :
                        cur = conn.cursor()
                        cur.execute(""" INSERT INTO backup_data(id,backup_name,backup_date,status) VALUES(?,?,?,?) """,
                                    (uid,name+".zip",now_for_db,"OK"))
                        conn.commit()
                    return True
            else :
                logger.error("Origin path not found!")
                return False
        except Exception as e :
            logger.critical(f"Backup failed! : {e}")
            return False
