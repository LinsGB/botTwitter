import mysql.connector
from database import host,user,password

class DbConnector():
    def __init__ (self):
        self.host     = host
        self.user     = user 
        self.password = password
    
    def buildConnector(self):
        try:
            mydb = mysql.connector.connect(
                    host     = host,
                    user     = user,
                    password = password   
                )
            #print("MYSQL CONNECTOR OK")
            return mydb

        except:
            #print("MYSQL CONNECTOR ERROR")
            return False
    
    



