#!/usr/bin/python3
from datetime import datetime
import requests
from os import path,mkdir 

# Check if Dev Mode
inTestMode = (True if path.isfile("dev") else False)


ip = requests.get('http://ip.42.pl/raw').text

# Check if Log Folder exist if not creates one, creates a log file

# Logging Function 
def log(msg: str):
    if not path.isdir("logs"):
        mkdir("logs")
    logname = "logfile-{}.log".format(datetime.now().strftime("%H-%M-%S"))
    logfile = open("{}\{}".format("logs",logname),"w",encoding="utf-8")
    time = datetime.now().strftime("%H:%M:%S")
    logfile.write("{}: {}".format(time,msg))
    print("{}: {}".format(time,msg))

# Reads Config File 
def readConfig():
    configparams = {}
    configname = ("config" if not inTestMode else "config_dev")
    try:
        configfile = open(configname,"r").read()
    except FileNotFoundError as e:
        log("Config Datei wurde nicht gefunden, Test Modus: {}".format(inTestMode))
    for f in configfile.split("\n"):
        vals : str = f.split(":")
        configparams[vals[0].strip()] = vals[1].strip()
    return configparams


configFile = readConfig()
ip = requests.get('http://ip.42.pl/raw').text
if ip != configFile["ip"]:
    log("IP Adresse hat sich geändert {} ==> {} \nAdmin wird {} wird kontaktiert".format( configFile["ip"],ip,configFile["alertmail"]))
    from sendmail import mailSender
    mail = mailSender(configFile)
    mail.sendMail()








