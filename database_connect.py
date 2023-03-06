# CONNECT TO DATABASE
import mysql.connector
from datetime import datetime

class DB:
    def __del__(self):
        self.db.close()

    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="adsorptech", # NAME OF USER
        passwd="root", # PASSWORD
        database="pilotplant" # DATABASE NAME
    )
        
    def addValue(self, Value, Name): # UPDATES VALUE AND TIME
        mycursor = self.db.cursor()
        mycursor.execute("UPDATE PilotTags SET Date = %s, Value = %s WHERE Name = %s",(datetime.now(), 5, Name))
        self.db.commit()
 

    def formatTable(self, Name, Datatype, Address):
        mycursor = self.db.cursor()
        mycursor.execute("INSERT IGNORE INTO PilotTags (Name, Datatype, Address, Date, Value) VALUES (%s, %s, %s, %s, NULL)", (Name, Datatype, Address, datetime.now()))
        self.db.commit()
 
    def createTable(self):
        mycursor = self.db.cursor()
        mycursor.execute("CREATE TABLE PilotTags (Name VARCHAR(50) PRIMARY KEY, Datatype VARCHAR(10) NOT NULL, Address VARCHAR(10) NOT NULL, Date DATETIME NOT NULL, Value DECIMAL(5,4))")
        self.db.commit
