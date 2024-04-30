# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 17:19:10 2022

@author: jkern
"""

import pandas as pd
import numpy as np

years = range(2000,2020)

df_nodes = pd.read_csv('../../WECC/nodal_wind.csv',header=0)
nodes = list(df_nodes.columns)
output = np.zeros((8760,len(nodes)))

for y in years:
    
    fn = 'nodal_hydro_' + str(y) + '.csv'
    df = pd.read_csv(fn,header=0)
    
    for n in nodes:
        
        idx = nodes.index(n)
        
        d = df.filter(like = n)
        
        if d.empty:
            pass
        
        else:
            
            a = d.sum(axis=1).values
            
            if y < 2019:
                output[0:8736,idx] = a[0:8736]
                output[8736:,idx] = a[8712:8736]
            else:
                output[0:8568,idx] = a[0:8568]
                output[8568:,idx] = a[-192:]
            
    df_out = pd.DataFrame(output)
    df_out.columns = nodes
    
    fn2 = 'nodal_hydro_' + str(y) + '_new.csv'
    df_out.to_csv(fn2,index=None)
    
    