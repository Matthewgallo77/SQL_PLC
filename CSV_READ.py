import pandas as pd
import snap7
from snap7.exceptions import Snap7Exception

import main
import utilities

data_frame = pd.read_csv(main.path) # CREATE DATAFAME OBJECT
# PUT IN NAME OF COLUMN 

addresses = data_frame['Logical Address'] 
data_types = data_frame['Data Type']
name = data_frame['Name']

while True:
    try:
        for address, data_type in zip(addresses, data_types):
                value = 0
                value = utilities.PLC_READ(address, data_type) # READ AND RETURN VALUE

                # NOW WRITE TO DATABASE

    except Snap7Exception as e:
         print(f"PLC Exception: {e}")
         


    

       

    
    



