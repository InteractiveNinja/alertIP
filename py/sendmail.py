import smtplib
from smtplib import SMTPException
class mailSender:
    def __init__(self,configsvals):
        self.__alertMail : str = configsvals["alertmail"]
        self.__alertName : str = configsvals["alertname"]
        self.__sender : str = configsvals["sender"]
        self.__smtp : str = configsvals["smtp"]
        self.__port : str = configsvals["port"]
        self.__senderpass : str = configsvals["senderpass"]
    
    def sendMail(self):
        message = """From: {} <{}@{}>
To: {} <{}>
Subject: IP Alert

Die IP des Servers hat sich geaendert, bitte pruefe das nach und restarte das Programm

Das ist eine Automatisierte Email.
""".format(self.__sender,self.__sender,self.__smtp,self.__alertName,self.__alertMail)
        server = smtplib.SMTP(self.__smtp)
        server.sendmail(self.__sender,self.__alertMail,message)