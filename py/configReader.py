import os
from .logger import Logger, logType


class Reader:
    def __init__(self, logger: Logger):
        self.__log = logger
        self.__execPath = os.getcwd()
        self.__configFolder = "{}\config".format(self.__execPath)
        self.__configPath = "{}\config.cfg".format(self.__configFolder)
        self.__defaultConfig = "ip: {your public ip}\nchecktime: {check time in seconds}\nalertmail: {your admin mail}\nalertname: {Admin Name}\nsender: {sendermail}\nsenderpass: {sender smtp password}\nsmtp: {smtp host}\nport: {smtp port}"

        self.__checkFolder()
        self.__checkFile()

    def __checkFolder(self):
        try:
            if not os.path.exists(self.__configFolder):
                os.mkdir(self.__configFolder)
                self.__log.log("Config Folder has been generated at {}".format(
                    self.__configFolder), logType.success)
        except OSError:
            self.__log.log("Config Folder cant be generated",logType.error)
            quit()


    def __checkFile(self):
        try:
            if not os.path.exists(self.__configPath):
                f = open(self.__configPath, "w")
                f.write(self.__defaultConfig)
                f.close()
                self.__log.log("Config File has been generated at {} please Update it".format(
                    self.__configPath), logType.success)
                quit()
            else:
                self.__checkFileForNotDefault()
        except OSError:
            self.__log.log("Config File cant be generated",logType.error)
            quit()

    def __checkFileForNotDefault(self):
        f = open(self.__configPath, "r")
        config = f.read()
        if config == self.__defaultConfig:
            self.__log.log("Default Config is still Loaded, please Change it at {}".format(
                self.__configPath), logType.invalid)
            quit()
        for line in config.split("\n"):
            if "{" in line or "}" in line:
                print(line)
                self.__log.log("Default Config is still Loaded, please Change it at {}".format(
                self.__configPath), logType.invalid)
                quit()

    def readConfig(self):
        """Gibt ein Dictory mit alle Config Attributen zurück
        Folgende Werte sind zu finden\n
        ip          : IP Adresse die geprüft werden soll\n
        checktime   : Zeit in Sekunden bis zur nächsten Prüfung\n 
        alertmail   : Zu alamierende Email Adresse\n
        alertname   : Name des Admins
        sender      : Email Sender Benutzer\n
        senderpass  : Email Sender Passwort\n
        smtp        : SMTP Server IP/Hostname \n
        port        : SMTP Server Port"""
        configParams = {}
        try:
            f = open(self.__configPath, "r")
            config = f.read()
            for line in config.split("\n"):
                attrName, attrVal = line.split(":")
                configParams[attrName] = attrVal.strip()
            f.close()
        except:
            self.__log.log("Config File cant be read",logType.error)
            quit()
        return configParams
