import os
import shutil
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
                    return True
            else :
                logger.error("Origin path ot found!")
                return False
        except Exception as e :
            logger.critical(f"Backup failed! : {e}")
            return False
