# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np

df = pd.read_csv('EIA_bus_match.csv',header=0)
dams = list(df['EIA_ID'])
nodes = []

years = range(2000,2020)

missing = []

for i in dams:
    
    idx1 = dams.index(i)
    
    n = df.loc[df['EIA_ID']==i,'new bus']
    
    fn = 'dayahead_ror_' + str(i) + '.csv'
    
    try:
        
        df_DP = pd.read_csv(fn,header=0)
          
    except:
        
        FileNotFoundError()
        
        try:
    
            fn = 'dayahead_storage_' + str(i) + '.csv'
            df_DP = pd.read_csv(fn)
            
        except:
            
            missing.append(i)
            pass
        
IDs = []
for element in dams:
    if element not in missing:
        IDs.append(element)

for y in years:
    
    f = 'nodal_hydro_' + str(y)
    f2 = 's_hydro_' + str(y)
    
    nodes = []

    for i in IDs:
        
        idx1 = IDs.index(i)
        
        n = df.loc[df['EIA_ID']==i,'new bus']
        
        nodes.append(n.values[0])
        
        fn = 'dayahead_ror_' + str(i) + '.csv'
        
        try:
            
            df_DP = pd.read_csv(fn,header=0)
            
            print(str(idx1) + ' of ' + str(len(IDs)-1))
        
        except:
            
            FileNotFoundError()
            
            try:
        
                fn = 'dayahead_storage_' + str(i) + '.csv'
                df_DP = pd.read_csv(fn)
                print(str(idx1) + ' of ' + str(len(IDs)-1))
                
            except:
                
                pass
        
        selected = df_DP.loc[df_DP['forecast'] == 'synthetic',:]
        selected = selected.reset_index(drop=True)
        selected['Date']= pd.to_datetime(selected['week_commencing'])  
        
        price = np.array(selected['price_price'])
        revenue = np.array(selected['benefit_revenue'])
        gen_MWh = np.divide(revenue,price)
        
        selected['gen'] = gen_MWh
        Y = []
        
        for m in range(0,len(selected)):
            Y.append(selected.loc[m,'Date'].year)
        selected['Year'] = Y
        
        selected = selected.dropna(subset=['release_spill'])
        
        year_selected = np.array(selected.loc[selected['Year'] == y,'gen'])
        
        if idx1 < 1:
  
            locals()[f] = year_selected
            
        else: 
    
            locals()[f] = np.column_stack([locals()[f],year_selected])
    
    df2 = pd.DataFrame(locals()[f])
    df2.columns = nodes
    
    fn = 'nodal_hydro_' + str(y) + '.csv'
    
    df2.to_csv(fn,index=None)
    
    
            
    
    
    
    
    
    
    
    