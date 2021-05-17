import requests
from sys import exit
from .configReader import Reader
from .logger import Logger,logType
from .sendmail import mailSender
class Check:
    def __init__(self,logger: Logger,reader : Reader):
        self.__logger = logger
        self.__config = reader.readConfig()
    
    def checkIP(self):
        publicIP = requests.get('http://ip.42.pl/raw').text
        configPublicIP = self.__config["ip"]
        if publicIP == configPublicIP:
            self.__logger.log("IP hasn't changed",logType.success)
        else:
            self.__logger.log("IP has Changed {}=>{}, sending Alert Mail".format(configPublicIP,publicIP),logType.warning)
            mailSender(self.__config).sendMail()
            exit()







