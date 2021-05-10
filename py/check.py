import requests
from .configReader import Reader
from os import getcwd



ip = requests.get('http://ip.42.pl/raw').text


class Check:
    def __init__(self,logger):
        self.logger = logger
        self.config = Reader.readConfig()
        print("test")

    # Reads Config File 
    def readConfig(self):
        configparams = {}
        configname = ("config" if not inTestMode else "config_dev")
        try:
            configfile = open(configname,"r").read()
        except FileNotFoundError as e:
            self.log("Config Datei wurde nicht gefunden, Test Modus: {}".format(inTestMode))
        for f in configfile.split("\n"):
            vals : str = f.split(":")
            configparams[vals[0].strip()] = vals[1].strip()
        return configparams


    ip = requests.get('http://ip.42.pl/raw').text
    if ip != configFile["ip"]:
        log("IP Adresse hat sich geändert {} ==> {} \nAdmin wird {} wird kontaktiert".format( configFile["ip"],ip,configFile["alertmail"]))
        from sendmail import mailSender
        mail = mailSender(configFile)
        mail.sendMail()








