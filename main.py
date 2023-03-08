import snap7
import snap7
from snap7.util import *
import utilities
from snap7.exceptions import Snap7Exception
from database_connect import DB
import pandas as pd
from datetime import datetime
import time


if __name__ == '__main__':
    PLC = snap7.client.Client() # CREATE PLC INSTANCE
    tag_datatype = {'Int':2,'Real':4} # GLOBAL DICT OF DATA TYPE

    path = utilities.setPath() # SET PATH OF PLC
    data_frame = pd.DataFrame(pd.read_excel(path))
    addresses = data_frame['Logical Address'] 
    data_types = data_frame['Data Type']
    names = data_frame['Name']

    # utilities.connectPLC() # CONNECT PLC
    database = DB() # CREATE INSTANCE OF DATABASE
    DB.createTable(database) # CREATES TABLE TO STORE TAG INFORMATION
    utilities.formatEntireTable(database, names, data_types, addresses) # FORMATS THE TABLE PROPERLY
                      
    while PLC.get_connected():
        try:
            for address, data_type, name in zip(addresses, data_types, names): # lOOP THROUGH EACH TAG
                value = utilities.PLC_READ(address, data_type)
                time.sleep(1) # STOP FOR ONE SECOND
                DB.addValue(database, value, name)

        except Snap7Exception as e:
             print(f"PLC Error: {e}")
                          