# CONNECT TO DATABASE
import mysql.connector
from datetime import datetime

class DB:    

    def __init__(self):

        self.databaseName = 'pilotplant'
        self.host = 'localhost'
        self.user = 'adsorptech'
        self.password = 'root'

        self.db = mysql.connector.connect(
        host=self.host,
        user=self.user, # NAME OF USER
        passwd=self.password, # PASSWORD
        database=self.databaseName # DATABASE NAME
    )

    def addValue(self, Value, Name): # UPDATES VALUE AND TIME
        mycursor = self.db.cursor()
        mycursor.execute(f"UPDATE {self.databaseName} SET Date = %s, Value = %s WHERE Name = %s",(datetime.now(), Value, Name))
        self.db.commit()
 

    def formatTable(self, Name, Datatype, Address):
        mycursor = self.db.cursor()
        mycursor.execute(f"INSERT IGNORE INTO {self.databaseName} (Name, Datatype, Address, Date, Value) VALUES (%s, %s, %s, %s, NULL)", (Name, Datatype, Address, datetime.now()))
        self.db.commit()
 
    def createTable(self):
        mycursor = self.db.cursor()
        mycursor.execute(f"CREATE TABLE IF NOT EXISTS {self.databaseName} (Name VARCHAR(50) PRIMARY KEY, Datatype VARCHAR(10) NOT NULL, Address VARCHAR(10) NOT NULL, Date DATETIME NOT NULL, Value DECIMAL(8,5))")
        self.db.commit


    def createPastTable(self):
        mycursor = self.db.cursor()
        query = "CREATE TABLE IF NOT EXISTS TagHistory (Date DATETIME NOT NULL, "
        