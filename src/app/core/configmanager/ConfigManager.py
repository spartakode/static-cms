import configparser

def getConfigurations():
    config = configparser.RawConfigParser()
    config.read("src/config.ini")
    return config

