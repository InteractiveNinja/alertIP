

import time
from sys import argv
from py.logger import Logger
from py.configReader import Reader
from py.check import Check
from py.argParser import passArgs
if(__name__ == "__main__"):
    noLog = passArgs(argv)
    logger = Logger(noLog)
    reader = Reader(logger)
    checker = Check(logger,reader)
    checkTime = reader.readConfig()["checktime"]
    while(True):
        checker.checkIP()
        time.sleep(checkTime)



