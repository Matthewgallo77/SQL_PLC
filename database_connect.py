# CONNECT TO DATABASE

import mysql.connector

db = mysql.connector.connect(
    host="", # NAME OF HOST
    user="", # NAME OF USER
    passwd="", # PASSWORD
    database="" # DATABASE NAME
)
