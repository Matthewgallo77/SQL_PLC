import snap7
import snap7
from snap7.util import *
import utilities
from snap7.exceptions import Snap7Exception
from database_connect import DB
import pandas as pd
from datetime import datetime


PLC = snap7.client.Client() # CREATE PLC INSTANCE
tag_datatype = {'Int':2,'Real':4} # GLOBAL DICT OF DATA TYPE

path = utilities.setPath() # SET PATH OF PLC
data_frame = pd.DataFrame(pd.read_excel(path))
addresses = data_frame['Logical Address'] 
data_types = data_frame['Data Type']
names = data_frame['Name']

utilities.connectPLC() # CONNECT PLC
# PUT IN NAME OF COLUMN 

x=0
database = DB() # CREATE INSTANCE OF DATABASE

for name, data_type, address in zip(names, data_types, addresses):
    database.formatTable(name, data_type, address)

main_cursor = database.db.cursor()

main_cursor.execute("SELECT * FROM PilotTags")
for x in main_cursor:
    print(x)