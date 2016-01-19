import socket
from configuration import Configuration
import mqtt.client as mqtt
import logging
import logging.config
import json
import os
import shell

Hostname = socket.gethostname()


def SetupLogging():
    path = "logging.json"
    if(os.path.exists(path)):
        with open(path, "rt") as file:
            config = json.load(file)

        logFileName = config.get("handlers", {}).get("timed_rotating_file_handler", {}).get("filename")
        if(not os.path.exists(logFileName)):
            #os.makedirs(logFileName)
            file = open(logFileName, "wt")
            file.close()

        logging.config.dictConfig(config)
    else:
        raise FileNotFoundError("Logging configuration")


def LoadConfiguration():
    configuration = Configuration(".config")
    return configuration.GetConfiguration()


def main():
    SetupLogging()
    config = LoadConfiguration()
    mqttClient = mqtt.Client
    myShell = shell.Shell(mqttClient=mqttClient, configuration=config)

    myShell.Run()

    return 0

if(__name__ == '__main__'):
    main()