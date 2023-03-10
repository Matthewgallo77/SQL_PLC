import re
import snap7
from snap7.util import *
from snap7.exceptions import Snap7Exception
from database_connect import DB
import database_connect

PLC = snap7.client.Client() # CREATE PLC INSTANCE
tag_datatype = {'Int':2,'Real':4} # GLOBAL DICT OF DATA TYPE

def getOffset(address):
    offset = re.sub("[^\d\.]", "", address).split('.')
    if len(offset) == 0:
        offset.append(0)
    
    return offset

def connectPLC():
    connected = False
    while not connected:
        try:
            IP = input("Enter the IP address of the PLC: ")
            PLC.connect(IP,0,1) # IP, RACK #, SLOT #
            print("CONNECTION STATUS: \nPLC is CONNECTED") # DISPLAYS IF CONNECTION TO PLC IS VALID
            connected = True
            return IP
        except Exception as e:
            print("CONNECTION STATUS: \nPLC is NOT CONNECTED\nCheck PLC connection or re-enter IP.")

def setPath():
    import os
    while True:
        path = input("Enter a path to a .xlsx file: ")
        if '.' not in path:
            path+='.xlsx'
        if os.path.exists(path):
            return path
        else:
            print("Invalid file path. Make sure file is in same directory. Please try again: \n")

def ReadData(byteArray, datatype): # M, MB, MW, MD
    if datatype == 'Real':
        return get_real(byteArray, 0)
    # elif datatype[0] == 'Bool':
        # return get_bool(byteArray, byte, bit)
    elif datatype == 'Int':
        return get_int(byteArray, 0)
    else:
        print(datatype)
        return 'ERROR: Data type has not been anticipated'
    
def PLC_READ(address, data_type):
    #   INPUT: ADDRESSES, DATA_TYPES
    #   FUNCTION: 
    #   READ PLC DATA AND STORE IN DATA FRAME TO USE IN DATABASE
    offset = getOffset(address) # GET OFFSET
    if 'I' in address:
        value = ReadData(PLC.read_area(snap7.types.Areas.PE, 0, int(offset[0]), tag_datatype[data_type]), data_type)
    elif 'M' in address:
        value = ReadData(PLC.read_area(snap7.types.Areas.MK, 0, int(offset[0]), tag_datatype[data_type]), data_type)
    elif 'Q' in address:
        value = ReadData(PLC.read_area(snap7.types.Areas.PA, 0, int(offset[0]), tag_datatype[data_type]), data_type)
    else:
        return print("Data type not anticipated, consult with Matt")
        
    return value

def formatEntireTable(database, names, data_types, addresses):
    for name, data_type, address in zip(names, data_types, addresses):
        database.formatTable(name, data_type, address)