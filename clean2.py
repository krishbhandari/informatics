# -*- coding: utf-8 -*-

import pandas as pd



#reads the excel file
hw1b = pd.read_excel('state_div_rate.xlsx',
                       skiprows=5,      #skips the first 5 rows                
                       header=[0],          #header is the 0th row         
                       skipfooter=4,         #skips the 4 footer rows          
                       usecols=22,           #the file has 22 columns A-V
                       index_col=[0])          #first col is treated as index 
                                                            

hw1b.dropna(how='all', inplace=True)   #drops rows will all null values
hw1b=hw1b.replace("---", "null")       #replaces string --- with string null

hw1b = hw1b.stack([0]).reset_index()   #pivots the table

hw1b.rename(columns={hw1b.columns[0] : 'State', #renames the name of the columns
                       hw1b.columns[1] : 'Year',
                       hw1b.columns[2] : 'Divorce Rate'},inplace=True)

#saves as new excel file
writer = pd.ExcelWriter('statedivorce-cleanNew.xlsx', engine='xlsxwriter') 
hw1b.to_excel(writer, sheet_name='Divorce Rates byState', index=False)
writer.save()


