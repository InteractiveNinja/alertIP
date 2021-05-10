import os
from .logger import Logger,logType

class Reader:
    def __init__(self, logger: Logger):
        self.__logger = logger
        self.__execPath = os.getcwd()
        self.__configFolder = "{}\config".format(self.__execPath)
        self.__configPath = "{}\config.cfg".format(self.__configFolder)

        self.__checkFolder()
        self.__checkFile()

    def __checkFolder(self):
        if not os.path.exists(self.__configFolder):
            os.mkdir(self.__configFolder)
            self.__logger.log("Config Folder has been generated at {}".format(
                self.__configFolder), logType.success)

    def __checkFile(self):
        if not os.path.exists(self.__configPath):
            f = open(self.__configPath, "w")
            f.write("ip: {your public ip}\nalertmail: {your admin mail}\nsender: {sendermail}\nsenderpass: {sender smtp password}\nsmtp: {smtp host}\nport: {smtp port}")
            self.__logger.log("Config File has been generated at {} please Update it".format(
                self.__configPath), logType.success)

    
    def readConfig(self):
        """Gibt ein Dictory mit alle Config Attributen zurück
        Folgende Werte sind zu finden\n
        ip: IP Adresse die geprüft werden soll\n
        alertmail: Zu alamierende Email Adresse\n
        sender: Email Sender Benutzer\n
        senderpass: Email Sender Passwort\n
        smtp: SMTP Server IP/Hostname \n
        port: SMTP Server Port"""
        configParams = {}
        config = open(self.__configPath, "r").read()
        for line in config.split("\n"):
            attrName,attrVal = line.split(":")
            configParams[attrName] = attrVal.strip()
        return configParams 
