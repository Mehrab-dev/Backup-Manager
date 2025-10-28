import datetime
import os
import shutil
import sqlite3
import uuid
from .config_logger import logger

class Backup() :
    def __init__(self,origin_path:str,destination_path:str) :
        self.origin_path = origin_path
        self.destination_path = destination_path
    def backup(self) :
        try :
            if os.path.exists(self.origin_path) :
                if os.path.isdir(self.origin_path) :
                    shutil.copytree(self.origin_path,self.destination_path)
                    logger.info("Folder successfully Backed up.")
                    uid = str(uuid.uuid4())
                    time = datetime.datetime.now().strftime("%y-%m-%d  %H:%M:%S")
                    name = f"backup in {time}"
                    dbpath = os.path.join(self.destination_path,"backup_data.sqlite3")
                    with sqlite3.connect(dbpath) as conn :
                        cur = conn.cursor()
                        cur.execute(""" INSERT INTO backup_data(id,backup_name,backup_date,backup_type,password,status)
                                        VALUES(?,?,?,?,?,?)""",(uid,name,time,"folder",None,True))
                        conn.commit()
                    return True
            else :
                logger.error("Origin path ot found!")
                return False
        except Exception as e :
            logger.critical(f"Backup failed! : {e}")
            return False
