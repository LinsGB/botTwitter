from database import DbConnector

def runComand( comand):
    try:
        dbConnector = DbConnector()
        mydb = dbConnector.buildConnector()
        cursor = mydb.cursor()
        cursor.execute(comand)
        #print("CURSOR EXECUTE OK")
        return True
    except:
        #print("CURSOR EXECUTE ERROR")
        return False

def runComandFetchall(comand):
    try:
        dbConnector = DbConnector()
        mydb = dbConnector.buildConnector()
        cursor = mydb.cursor()
        cursor.execute(comand)
        #print("CURSOR EXECUTE OK")
        return cursor.fetchall()
    except:
        #print("CURSOR EXECUTE ERROR")
        return False

def runComandCommit(comand, values):
    try:
        dbConnector = DbConnector()
        mydb = dbConnector.buildConnector()
        cursor = mydb.cursor()
        cursor.execute(comand, values)
        #print("CURSOR EXECUTE OK")
        mydb.commit()
        #print("COMMIT OK")
        return True
    except:
    #print("COMIT/CURSOR EXECUTE ERROR")
        return False
        
    