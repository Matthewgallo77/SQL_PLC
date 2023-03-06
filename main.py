import snap7
import snap7
from snap7.util import *
import utilities
from snap7.exceptions import Snap7Exception
import pandas as pd



PLC = snap7.client.Client() # CREATE PLC INSTANCE
tag_datatype = {'Int':2,'Real':4} # GLOBAL DICT OF DATA TYPE
if __name__ == '__main__':

    # path = utilities.setPath() # SET PATH OF PLC
    path = 'tags.xlsx'
    data_frame = pd.DataFrame(pd.read_excel(path))
    addresses = data_frame['Logical Address'] 
    data_types = data_frame['Data Type']
    name = data_frame['Name']
    utilities.connectPLC() # CONNECT PLC
    # PUT IN NAME OF COLUMN 
    while True:
        try:
            for address, data_type in zip(addresses, data_types):
                    value = 0
                    value = utilities.PLC_READ(address, data_type) # READ AND RETURN VALUE
                    print(value)
                    # NOW WRITE TO DATABASE

        except Snap7Exception as e:
            print(f"PLC Exception: {e}")
