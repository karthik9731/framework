import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\ckart\PycharmProjects\pythonProject1\fg_project\Configurations\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseUrl')
        return url

    @staticmethod
    def getUsermail():
        username = config.get("common info","username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info","password")
        return password