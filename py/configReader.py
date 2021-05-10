import os
from py.logger import Logger,logType

class Reader:
    def __init__(self,logger: Logger):
        exePath = os.getcwd()
        configFolder = "{}\config".format(exePath)
        configPath = "{}\config.cfg".format(configFolder)
        if not os.path.exists(configFolder):
            os.mkdir(configFolder)
            logger.log("Config Folder has been generated at {}".format(configFolder),logType.success)
        if not os._exists(configPath):
            f = open(configPath,"w")
            f.write("ip: {your public ip}\nalertmail: {your admin mail}\nsender: {sendermail}\nsenderpass: {sender smtp password}\nsmtp: {smtp host}\nport: {smtp port}")
            logger.log("Config File has been generated at {} please Update it".format(configPath),logType.success)
