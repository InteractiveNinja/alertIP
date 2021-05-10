from datetime import datetime
from os import path,mkdir 

class Logger:

    def __init__(self):
        self.logname = "logfile-{}.log".format(datetime.now().strftime("%H-%M-%S"))
        self.logfile = open("{}\{}".format("logs",logname),"w",encoding="utf-8")
        if not path.isdir("logs"):
            mkdir("logs")

    def log(self,msg:str):
        time = datetime.now().strftime("%H:%M:%S")
        self.logfile.write("{}: {}".format(time,msg))
        print("{}: {}".format(time,msg))