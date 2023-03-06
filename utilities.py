import re
import snap7
from snap7.util import *
from snap7.exceptions import Snap7Exception
import main

def getOffset(address):
    offset = re.sub("[^\d\.]", "", address).split('.')
    if len(offset) == 0:
        offset.append(0)
    
    return offset

def connectPLC(PLC):
    while (PLC.get_connected() != True):
        IP = input("Enter the IP address of the PLC: ")
        try:
            PLC.connect(IP,0,1) # IP, RACK #, SLOT #
            if PLC.get_connected():
                return True
        except:
            print("Invalid IP. Please try again: \n")

def setPath():
    import os
    while True:
        path = input("Enter a path to a .csv file: ")
        if os.path.exists(path) and path.endswith(".csv"):
            return path
        else:
            print("Invalid file path. Please try again: \n")


def ReadData(byteArray, datatype): # M, MB, MW, MD
    if datatype == 'Real':
        return get_real(byteArray, 0)
    # elif datatype[0] == 'Bool':
        # return get_bool(byteArray, byte, bit)
    elif datatype == 'Int':
        return get_int(byteArray, 0)
    else:
        return 'ERROR: Data type has not been anticipated'
    
def PLC_READ(address, data_type):
    #   INPUT: ADDRESSES, DATA_TYPES
    #   FUNCTION: 
    #   READ PLC DATA AND STORE IN DATA FRAME TO USE IN DATABASE
    offset = getOffset(address) # GET OFFSET
    if 'I' in address:
        value = ReadData(main.PLC.read_area(snap7.types.Areas.PE, 0, offset[0], main.tag_datatype[data_type]), main.tag_datatype[data_type])
    elif 'M' in address:
        value = ReadData(main.PLC.read_area(snap7.types.Areas.MK, 0, offset[0], main.tag_datatype[data_type]), main.tag_datatype[data_type])
    elif 'Q' in address:
        value = ReadData(main.PLC.read_area(snap7.types.Areas.PA, 0, offset[0], main.tag_datatype[data_type]), main.tag_datatype[data_type])
    else:
        return print("Data type not anticipated, consult with Matt")
        
    return value