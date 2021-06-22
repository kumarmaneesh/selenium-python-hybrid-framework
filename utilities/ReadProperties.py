import configparser

config = configparser.RawConfigParser()
config.read(".//Configurations/config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        return config.get('site info', 'baseURL')

    @staticmethod
    def getUsername():
        return config.get('site info', 'username')

    @staticmethod
    def getPassword():
        return config.get('site info', 'password')



