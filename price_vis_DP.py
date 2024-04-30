# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 01:34:45 2023

@author: jkern
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Get bus IDs
df = pd.read_csv('wsynthetic/wsynthetic/EIA_bus_match.csv',header=0)
dams = list(df['EIA_ID'])
nodes = []

years = range(2000,2020)

missing = []

for i in dams:
    
    idx1 = dams.index(i)
    
    n = df.loc[df['EIA_ID']==i,'new bus']
    
    fn = 'wsynthetic/wsynthetic/dayahead_ror_' + str(i) + '.csv'
    
    try:
        
        df_DP = pd.read_csv(fn,header=0)
          
    except:
        
        FileNotFoundError()
        
        try:
    
            fn = 'wsynthetic/wsynthetic/dayahead_storage_' + str(i) + '.csv'
            df_DP = pd.read_csv(fn)
            
        except:
            
            missing.append(i)
            pass
        
IDs = []
for element in dams:
    if element not in missing:
        IDs.append(element)
        
caps = []
buses = []

for i in IDs:
    
    c = df.loc[df['EIA_ID'] == i,'capacity'].values[0]
    b = df.loc[df['EIA_ID'] == i,'new bus'].values[0]
    
    if b in buses:
        idx = buses.index(b)
        caps[idx] += c
    
    else:
        
        caps.append(c)
        buses.append(b)
        
years = range(2000,2020)
scenarios = ['persistence','synthetic']
df_units = pd.read_csv('results_synthetic/duals_2000.csv',header=0)
units = list(df_units['Bus'].unique())

full_caps = []
for u in units:
    if u in buses:
        idx = buses.index(u)
        full_caps.append(caps[idx])
    else:
        full_caps.append(0)
        
persistence_output = np.zeros((8736,len(units)))
synthetic_output = np.zeros((8736,len(units)))




fig_persistence, axs1 = plt.subplots(5,4,figsize=(12,18))
fig_persistence2, axs2 = plt.subplots(5,4,figsize=(12,18))

for y in years:
    
    stds = []
    
    fn = 'results_perfect/' + 'duals_' + str(y) + '.csv'
    df_pf = pd.read_csv(fn,header=0)
    
    for s in ['persistence']:
        
        s_idx = scenarios.index(s)
        
        fn = 'results_' + s + '/duals_' + str(y) + '.csv'
        
        df = pd.read_csv(fn,header=0)
        
        for u in units:
        
            sample1 = df.loc[df['Bus'] == u,'Value'].values
            sample2 = df_pf.loc[df['Bus'] == u,'Value'].values
            diff = sample1-sample2
            
            if s == 'persistence':
                persistence_output[:,s_idx] = diff
                
            elif s == 'synthetic':
                synthetic_output[:,s_idx] = diff
                
            stds.append(np.std(diff))
                
            
    if y == 2000:

        axs1[0,0].plot(persistence_output)  
        axs1[0,0].set_title('Persistence ' + 'Year = ' + str(y))
    
    elif y == 2001:
        
        axs1[0,1].plot(persistence_output)  
        axs1[0,1].set_title('Persistence ' + 'Year = ' + str(y))
    
    elif y == 2002:
                    
        axs1[0,2].plot(persistence_output)  
        axs1[0,2].set_title('Persistence ' + 'Year = ' + str(y))

    elif y == 2003:
                    
        axs1[0,3].plot(persistence_output)  
        axs1[0,3].set_title('Persistence ' + 'Year = ' + str(y))
    
    elif y == 2004:
                    
        axs1[1,0].plot(persistence_output)  
        axs1[1,0].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2005:
                    
        axs1[1,1].plot(persistence_output)  
        axs1[1,1].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2006:
                    
        axs1[1,2].plot(persistence_output)  
        axs1[1,2].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2007:
                    
        axs1[1,3].plot(persistence_output)  
        axs1[1,3].set_title('Persistence ' + 'Year = ' + str(y))
            
    elif y == 2008:
                    
        axs1[2,0].plot(persistence_output)  
        axs1[2,0].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2009:
                    
        axs1[2,1].plot(persistence_output)  
        axs1[2,1].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2010:
                    
        axs1[2,2].plot(persistence_output)  
        axs1[2,2].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2011:
                    
        axs1[2,3].plot(persistence_output)  
        axs1[2,3].set_title('Persistence ' + 'Year = ' + str(y))

    elif y == 2012:
                    
        axs1[3,0].plot(persistence_output)  
        axs1[3,0].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2013:
                    
        axs1[3,1].plot(persistence_output)  
        axs1[3,1].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2014:
                    
        axs1[3,2].plot(persistence_output)  
        axs1[3,2].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2015:
                    
        axs1[3,3].plot(persistence_output)  
        axs1[3,3].set_title('Persistence ' + 'Year = ' + str(y))

    elif y == 2016:
                    
        axs1[4,0].plot(persistence_output)  
        axs1[4,0].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2017:
                    
        axs1[4,1].plot(persistence_output)  
        axs1[4,1].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2018:
                    
        axs1[4,2].plot(persistence_output)  
        axs1[4,2].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2019:
                    
        axs1[4,3].plot(persistence_output)  
        axs1[4,3].set_title('Persistence ' + 'Year = ' + str(y))
            
      
    for ax in axs1.flat:
       ax.set(xlabel='Hour', ylabel='Difference from Perfect ($/MWh)')
      
        
# SCATTERPLOTS  
        
    if y == 2000:
    
        axs2[0,0].scatter(full_caps,stds)  
        axs2[0,0].set_title('Persistence ' + 'Year = ' + str(y))
    
    elif y == 2001:
        
        axs2[0,1].scatter(full_caps,stds)  
        axs2[0,1].set_title('Persistence ' + 'Year = ' + str(y))
    
    elif y == 2002:
                    
        axs2[0,2].scatter(full_caps,stds)  
        axs2[0,2].set_title('Persistence ' + 'Year = ' + str(y))
    
    elif y == 2003:
                    
        axs2[0,3].scatter(full_caps,stds)  
        axs2[0,3].set_title('Persistence ' + 'Year = ' + str(y))
    
    elif y == 2004:
                    
        axs2[1,0].scatter(full_caps,stds)  
        axs2[1,0].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2005:
                    
        axs2[1,1].scatter(full_caps,stds)  
        axs2[1,1].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2006:
                    
        axs2[1,2].scatter(full_caps,stds)  
        axs2[1,2].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2007:
                    
        axs2[1,3].scatter(full_caps,stds)  
        axs2[1,3].set_title('Persistence ' + 'Year = ' + str(y))
            
    elif y == 2008:
                    
        axs2[2,0].scatter(full_caps,stds)  
        axs2[2,0].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2009:
                    
        axs2[2,1].scatter(full_caps,stds)  
        axs2[2,1].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2010:
                    
        axs2[2,2].scatter(full_caps,stds)  
        axs2[2,2].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2011:
                    
        axs2[2,3].scatter(full_caps,stds)  
        axs2[2,3].set_title('Persistence ' + 'Year = ' + str(y))
    
    elif y == 2012:
                    
        axs2[3,0].scatter(full_caps,stds)  
        axs2[3,0].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2013:
                    
        axs2[3,1].scatter(full_caps,stds)  
        axs2[3,1].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2014:
                    
        axs2[3,2].scatter(full_caps,stds)  
        axs2[3,2].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2015:
                    
        axs2[3,3].scatter(full_caps,stds)  
        axs2[3,3].set_title('Persistence ' + 'Year = ' + str(y))
    
    elif y == 2016:
                    
        axs2[4,0].scatter(full_caps,stds)  
        axs2[4,0].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2017:
                    
        axs2[4,1].scatter(full_caps,stds)  
        axs2[4,1].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2018:
                    
        axs2[4,2].scatter(full_caps,stds)  
        axs2[4,2].set_title('Persistence ' + 'Year = ' + str(y))
        
    elif y == 2019:
                    
        axs2[4,3].scatter(full_caps,stds)  
        axs2[4,3].set_title('Persistence ' + 'Year = ' + str(y))
            
      
    for ax in axs2.flat:
       ax.set(xlabel='Hydro Capacity (MWh)', ylabel='Std. Deviation')    
            
      
        
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs1.flat:
    ax.label_outer()   
  
plt.savefig('persistence.png',dpi=200)

for ax in axs2.flat:
    ax.label_outer()   
  
plt.savefig('scatter_persistence.png',dpi=200)



                
            
fig_synthetic, axs1 = plt.subplots(5,4,figsize=(12,18))
fig_synthetic2, axs2 = plt.subplots(5,4,figsize=(12,18))

for y in years:
    
    stds = []
    
    fn = 'results_perfect/' + 'duals_' + str(y) + '.csv'
    df_pf = pd.read_csv(fn,header=0)
    
    for s in ['synthetic']:
        
        s_idx = scenarios.index(s)
        
        fn = 'results_' + s + '/duals_' + str(y) + '.csv'
        
        df = pd.read_csv(fn,header=0)
        
        for u in units:
        
            sample1 = df.loc[df['Bus'] == u,'Value'].values
            sample2 = df_pf.loc[df['Bus'] == u,'Value'].values
            diff = sample1-sample2
            
            if s == 'synthetic':
                synthetic_output[:,s_idx] = diff
                
            elif s == 'synthetic':
                synthetic_output[:,s_idx] = diff
                
            stds.append(np.std(diff))
                
            
    if y == 2000:

        axs1[0,0].plot(synthetic_output)  
        axs1[0,0].set_title('synthetic ' + 'Year = ' + str(y))
    
    elif y == 2001:
        
        axs1[0,1].plot(synthetic_output)  
        axs1[0,1].set_title('synthetic ' + 'Year = ' + str(y))
    
    elif y == 2002:
                    
        axs1[0,2].plot(synthetic_output)  
        axs1[0,2].set_title('synthetic ' + 'Year = ' + str(y))

    elif y == 2003:
                    
        axs1[0,3].plot(synthetic_output)  
        axs1[0,3].set_title('synthetic ' + 'Year = ' + str(y))
    
    elif y == 2004:
                    
        axs1[1,0].plot(synthetic_output)  
        axs1[1,0].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2005:
                    
        axs1[1,1].plot(synthetic_output)  
        axs1[1,1].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2006:
                    
        axs1[1,2].plot(synthetic_output)  
        axs1[1,2].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2007:
                    
        axs1[1,3].plot(synthetic_output)  
        axs1[1,3].set_title('synthetic ' + 'Year = ' + str(y))
            
    elif y == 2008:
                    
        axs1[2,0].plot(synthetic_output)  
        axs1[2,0].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2009:
                    
        axs1[2,1].plot(synthetic_output)  
        axs1[2,1].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2010:
                    
        axs1[2,2].plot(synthetic_output)  
        axs1[2,2].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2011:
                    
        axs1[2,3].plot(synthetic_output)  
        axs1[2,3].set_title('synthetic ' + 'Year = ' + str(y))

    elif y == 2012:
                    
        axs1[3,0].plot(synthetic_output)  
        axs1[3,0].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2013:
                    
        axs1[3,1].plot(synthetic_output)  
        axs1[3,1].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2014:
                    
        axs1[3,2].plot(synthetic_output)  
        axs1[3,2].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2015:
                    
        axs1[3,3].plot(synthetic_output)  
        axs1[3,3].set_title('synthetic ' + 'Year = ' + str(y))

    elif y == 2016:
                    
        axs1[4,0].plot(synthetic_output)  
        axs1[4,0].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2017:
                    
        axs1[4,1].plot(synthetic_output)  
        axs1[4,1].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2018:
                    
        axs1[4,2].plot(synthetic_output)  
        axs1[4,2].set_title('synthetic ' + 'Year = ' + str(y))
        
    elif y == 2019:
                    
        axs1[4,3].plot(synthetic_output)  
        axs1[4,3].set_title('synthetic ' + 'Year = ' + str(y))
            
      
    for ax in axs1.flat:
       ax.set(xlabel='Hour', ylabel='Difference from Perfect ($/MWh)')
      
        
# SCATTERPLOTS  
        
    if y == 2000:
    
        axs2[0,0].scatter(full_caps,stds)  
        axs2[0,0].set_title('Synthetic ' + 'Year = ' + str(y))
    
    elif y == 2001:
        
        axs2[0,1].scatter(full_caps,stds)  
        axs2[0,1].set_title('Synthetic ' + 'Year = ' + str(y))
    
    elif y == 2002:
                    
        axs2[0,2].scatter(full_caps,stds)  
        axs2[0,2].set_title('Synthetic ' + 'Year = ' + str(y))
    
    elif y == 2003:
                    
        axs2[0,3].scatter(full_caps,stds)  
        axs2[0,3].set_title('Synthetic ' + 'Year = ' + str(y))
    
    elif y == 2004:
                    
        axs2[1,0].scatter(full_caps,stds)  
        axs2[1,0].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2005:
                    
        axs2[1,1].scatter(full_caps,stds)  
        axs2[1,1].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2006:
                    
        axs2[1,2].scatter(full_caps,stds)  
        axs2[1,2].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2007:
                    
        axs2[1,3].scatter(full_caps,stds)  
        axs2[1,3].set_title('Synthetic ' + 'Year = ' + str(y))
            
    elif y == 2008:
                    
        axs2[2,0].scatter(full_caps,stds)  
        axs2[2,0].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2009:
                    
        axs2[2,1].scatter(full_caps,stds)  
        axs2[2,1].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2010:
                    
        axs2[2,2].scatter(full_caps,stds)  
        axs2[2,2].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2011:
                    
        axs2[2,3].scatter(full_caps,stds)  
        axs2[2,3].set_title('Synthetic ' + 'Year = ' + str(y))
    
    elif y == 2012:
                    
        axs2[3,0].scatter(full_caps,stds)  
        axs2[3,0].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2013:
                    
        axs2[3,1].scatter(full_caps,stds)  
        axs2[3,1].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2014:
                    
        axs2[3,2].scatter(full_caps,stds)  
        axs2[3,2].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2015:
                    
        axs2[3,3].scatter(full_caps,stds)  
        axs2[3,3].set_title('Synthetic ' + 'Year = ' + str(y))
    
    elif y == 2016:
                    
        axs2[4,0].scatter(full_caps,stds)  
        axs2[4,0].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2017:
                    
        axs2[4,1].scatter(full_caps,stds)  
        axs2[4,1].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2018:
                    
        axs2[4,2].scatter(full_caps,stds)  
        axs2[4,2].set_title('Synthetic ' + 'Year = ' + str(y))
        
    elif y == 2019:
                    
        axs2[4,3].scatter(full_caps,stds)  
        axs2[4,3].set_title('Synthetic ' + 'Year = ' + str(y))
            
      
    for ax in axs2.flat:
       ax.set(xlabel='Hydro Capacity (MWh)', ylabel='Std. Deviation')    
            
      
        
# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs1.flat:
    ax.label_outer()   
  
plt.savefig('synthetic.png',dpi=200)

for ax in axs2.flat:
    ax.label_outer()   
  
plt.savefig('scatter_synthetic.png',dpi=200)

df = pd.DataFrame()
df['buses'] = units
df['stds'] = stds
df.to_csv('for_map.csv',index=None)

