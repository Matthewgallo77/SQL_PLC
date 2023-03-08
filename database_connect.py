# CONNECT TO DATABASE
import mysql.connector
from datetime import datetime

class DB:    

    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root", # NAME OF USER
        passwd="notforu;)", # PASSWORD
        database="test" # DATABASE NAME
    )

    def addValue(self, Value, Name): # UPDATES VALUE AND TIME
        mycursor = self.db.cursor()
        mycursor.execute("UPDATE TagTable SET Date = %s, Value = %s WHERE Name = %s",(datetime.now(), Value, Name))
        self.db.commit()
 

    def formatTable(self, Name, Datatype, Address):
        mycursor = self.db.cursor()
        mycursor.execute("INSERT IGNORE INTO TagTable (Name, Datatype, Address, Date, Value) VALUES (%s, %s, %s, %s, NULL)", (Name, Datatype, Address, datetime.now()))
        self.db.commit()
 
    def createTable(self):
        mycursor = self.db.cursor()
        mycursor.execute("CREATE TABLE IF NOT EXISTS TagTable (Name VARCHAR(50) PRIMARY KEY, Datatype VARCHAR(10) NOT NULL, Address VARCHAR(10) NOT NULL, Date DATETIME NOT NULL, Value DECIMAL(8,5))")
        self.db.commit
