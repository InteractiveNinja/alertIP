from datetime import datetime
from os import path,mkdir,getcwd

from enum import Enum
class logType(Enum):
    success = 0
    warning = 1
    log     = 2
    invalid = 3
    error   = 4
class Logger:

    def __init__(self,noLog: bool):
        self.__noLog = noLog
        if noLog : print("File Logging is with --no-log disabled")
        if not noLog:
            self.__logpath = "{}\logs".format(getcwd())
            if not path.isdir(self.__logpath):
                mkdir("logs")
            self.__logname = "{}.log".format(datetime.now().strftime("%H-%M-%S"))
            self.__logfile = open("{}\{}".format(self.__logpath,self.__logname),"w",encoding="utf-8")
            self.__logfile.write("--------- Begin of Log ---------\n")
            

    def log(self,msg:str,logType : logType):
        time = datetime.now().strftime("%H:%M:%S")
        msgStr = "[{}] {}: {}\n".format(logType.name,time,msg)
        if not self.__noLog:
            self.__logfile.write(msgStr)
        print(msgStr)

