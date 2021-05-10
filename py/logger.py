from datetime import datetime
from os import path,mkdir,getcwd

from enum import Enum
class errorcode(Enum):
    success = 0
    warning = 1
    log     = 2
    invalid = 3
class Logger:

    def __init__(self):
        self.logpath = "{}\logs".format(getcwd())
        if not path.isdir(self.logpath):
            mkdir("logs")
        self.logname = "{}.log".format(datetime.now().strftime("%H-%M-%S"))
        self.logfile = open("{}\{}".format(self.logpath,self.logname),"w",encoding="utf-8")
        self.logfile.write("--------- Begin of Log ---------\n")
       

    def log(self,msg:str,logType : errorcode):
        time = datetime.now().strftime("%H:%M:%S")
        msgStr = "[{}] {}: {}\n".format(logType.name,time,msg)
        self.logfile.write(msgStr)
        print(msgStr)

