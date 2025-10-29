import os
import shutil
import datetime
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
                    if not os.path.exists(self.destination_path) :
                        os.makedirs(self.destination_path,exist_ok=True)
                    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    name = os.path.join(self.destination_path,now)
                    shutil.make_archive(name,"zip",self.origin_path)
                    logger.info(f"Folder successfully Backed up as {name}.zip")
                    uid = str(uuid.uuid4())
                    with sqlite3.connect("backup_data.sqlite3") as conn :
                        cur = conn.cursor()
                        cur.execute(""" INSERT INTO backup_data(id,backup_name,backup_date,backup_type,status) VALUES(?,?,?,?,?) """,
                                    (uid,name+".zip",now,"Folder",True))
                        conn.commit()
                    return True
            else :
                logger.error("Origin path not found!")
                return False
        except Exception as e :
            logger.critical(f"Backup failed! : {e}")
            return False
