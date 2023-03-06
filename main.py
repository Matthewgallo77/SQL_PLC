import snap7
import snap7
from snap7.util import *
import utilities

if __name__ == '__main__':
    tag_datatype = {'Int':2,'Real':4} # GLOBAL DICT OF DATA TYPES
    PLC = snap7.client.Client() # CREATE PLC INSTANCE
    utilities.connectPLC(PLC) # CONNECT PLC
    path = utilities.setPath() # SET PATH OF PLC
