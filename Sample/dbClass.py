class DbConf:
    def __init__(self):
        self.__host = "localhost"
        self.__user = "dbtDev65r2" #user name
        self.__password = "Miss6145" #user password
        self.__dbname = "dbSample65r2" #database name

    def getHost(self):
        return self.__host

    def getUser(self):
        return self.__user

    def getPassword(self):
        return self.__password

    def getDbName(self):
        return self.__dbname