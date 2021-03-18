#!/usr/bin/python3
from datetime import datetime
import requests
from os import path,mkdir 

# Check if Dev Mode
inTestMode = (True if path.isfile("dev") else False)
print(inTestMode)


ip = requests.get('http://ip.42.pl/raw').text

# Check if Log Folder exist if not creates one, creates a log file
if not path.isdir("logs"):
    mkdir("logs")
logname = "logfile-{}.log".format(datetime.now().strftime("%H-%M-%S"))
logfile = open("{}\{}".format("logs",logname),"w")
# Logging Function 
def log(msg: str):
    time = datetime.now().strftime("%H:%M:%S")
    logfile.write("{}: {}".format(time,msg))

# Reads Config File 
def readConfig():
    configparams = {}
    configname = ("config" if inTestMode else "config_dev")
    configfile = open(configname,"r").read()
    for f in configfile.split("\n"):
        vals : str = f.split(":")
        configparams[vals[0].strip()] = vals[1].strip()
    return configparams


configFile = readConfig()







