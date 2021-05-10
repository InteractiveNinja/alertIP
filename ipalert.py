

import time
from sys import argv
from py.logger import Logger, logType
from py.configReader import Reader
from py.check import Check
from py.argParser import passArgs
if(__name__ == "__main__"):
    noLog = passArgs(argv)
    logger = Logger(noLog)
    reader = Reader(logger)
    checker = Check(logger,reader)
    try:
        checkTime = int(reader.readConfig()["checktime"])
    except:
        logger.log("Parsing Error from Checktime, please look at the Configfile",logType.error)
        quit()
    while(True):
        checker.checkIP()
        time.sleep(checkTime)



