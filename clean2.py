# -*- coding: utf-8 -*-

import pandas as pd




hw1b = pd.read_excel('state_div_rate.xlsx',
                       skiprows=5,                      
                       header=[0],                   
                       skipfooter=4,                   
                       usecols=22,
                       index_col=[0])           
                                                            

hw1b.dropna(how='all', inplace=True)
hw1b=hw1b.replace("---", "null")

hw1b = hw1b.stack([0]).reset_index()

hw1b.rename(columns={hw1b.columns[0] : 'State',
                       hw1b.columns[1] : 'Year',
                       hw1b.columns[2] : 'Divorce Rate'},inplace=True)

##### dataframe to excel file
writer = pd.ExcelWriter('statedivorce-cleanNew.xlsx', engine='xlsxwriter')
hw1b.to_excel(writer, sheet_name='Divorce Rates byState', index=False)
writer.save()


